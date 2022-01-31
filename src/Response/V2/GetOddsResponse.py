#region Imports
import json;
from Models.V2 import Game, Odds;
from Base import ResponseBase
#endregion Imports

class GetOddsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        resp = json.loads(response);
        self.Odds = self.ParseResponse(json.dumps(resp['data']));
        self.Type = 'American';
        
    def ParseResponse(self, response:str):
        try:
            obj = json.loads(response);
            games = [Game.fromDict(m) for m in obj]; 
            for f in games:
                f.odds = [Odds.fromDict(m) for m in f.odds]
            return games;
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