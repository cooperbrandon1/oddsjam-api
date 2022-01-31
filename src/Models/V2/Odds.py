#region Imports
from dataclasses import dataclass;
from Models.V2 import Game;
from Base import ModelBase;
#endregion Imports

@dataclass
class Odds(ModelBase):
    id: str = None;
    sports_book_name: str = None;
    market_name: str = None;
    name: str = None;
    price: float = None;
    is_main: bool = None;
    is_live: bool = None;
    checked_date: str = None;
    __type__ = 'American';
    
    def AsDecimal(self):
        try:
            if(self.__type__ != 'Decimal'):
                if(self.price < 0):
                    self.price = 1 + (100/(self.price*-1))
                elif self.price > 0:
                    self.price = (self.price/100) + 1
                self.__type__ = 'Decimal'
            else:
                print('Already decimal');
        except Exception as ex:
            return ex;
    
    def AsAmerican(self):
        try:
            if(self.__type__ != 'American'):
                if(self.__type__ == 'Decimal'):
                    if(self.price > 2):
                        self.price = (self.price - 1) * 100
                    else:
                        self.price = (-100) / (self.price-1)
                    self.price = round(self.price,1);
                self.__type__ = 'American'
            else:
                print('Already American')
        except Exception as ex:
            return ex;