#region Imports
import datetime
from Enum.SportsBooksEnum import SportsBooksEnum
from Models.Game import Game;
from Base import ModelBase
#endregion Imports

class Odds(ModelBase):
    def __init__(self,game: Game = None, market_name: str = None, sports_book: SportsBooksEnum = None, name: str = None, 
    price: float = None, is_main: bool = None, is_live: bool = None, checked_date: datetime = None, changed_date: datetime = None):
        self._game = game;
        self._marketName = market_name;
        self._sportsBook = sports_book;
        self._name = name;
        self._price = price;
        self._isMain = is_main;
        self._isLive = is_live;
        self._checkedDate = checked_date;
        self._changedDate = changed_date;


    @property
    def Game(self):
        return self._game;
    
    @Game.setter
    def Game(self, newGame: Game):
        self._game = newGame;

    @property
    def MarketName(self):
        return self._marketName;
    
    @MarketName.setter
    def MarketName(self, newMarketName:str):
        self._marketName = newMarketName;

    @property
    def SportsBook(self):
        return self._sportsBook;
    
    @SportsBook.setter
    def SportsBook(self, newSportsBook: SportsBooksEnum):
        self._sportsBook = newSportsBook

    @property
    def Name(self):
        return self._name;

    @Name.setter
    def Name(self, newName: str):
        self._name = newName;

    @property
    def Price(self):
        return self._price;

    @Price.setter
    def Price(self, newPrice: float):
        self._price = newPrice;

    @property
    def IsMain(self):
        return self._isMain;
    
    @IsMain.setter
    def IsMain(self, newIsMain: bool):
        self._isMain = newIsMain;

    @property
    def IsLive(self):
        return self._isLive;
    
    @IsLive.setter
    def IsLive(self, newIsLive: bool):
        self._isLive = newIsLive;

    @property
    def CheckedDate(self):
        return self._checkedDate;

    @CheckedDate.setter
    def CheckedDate(self, newCheckedDate: datetime):
        self._checkedDate = newCheckedDate;

    @property
    def ChangedDate(self):
        return self._changedDate;

    @ChangedDate.setter
    def ChangedDate(self, newChangedDate:datetime):
        self._changedDate = newChangedDate;