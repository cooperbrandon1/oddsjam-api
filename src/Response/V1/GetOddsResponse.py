#region Imports
import json;
from Models.V1 import Odds, Game;
from Base import ResponseBase;
#endregion Imports

class GetOddsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        self.Odds = self.ParseResponse(response);
        self.Type = 'American';
        
    def ParseResponse(self, response:str):
        try:
            obj = json.loads(response);
            oddsObjects = [Odds.fromDict(m) for m in obj];
            for o in oddsObjects:
                o.game = Game.fromDict(o.game);
                o.sports_book = o.sports_book['name']
            return oddsObjects;
        except Exception as ex:
            return ex;

    def AsDecimal(self):
        try:
            [o.AsDecimal() for o in self.Odds]
        except Exception as ex:
            return ex;
    
    def AsAmerican(self):
        try:
            [o.AsAmerican() for o in self.Odds]
        except Exception as ex:
            return ex;