#region Imports
import json;
import collections;
from Models import Odds;
from Base import ResponseBase;
#endregion Imports

class GetOddsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        self.Odds = self.ParseResponse(response);

    def GetPrices(self):
        '''Returns all prices in the response'''
        return [o.Price for o in self.Odds]

    def GetGameIDs(self):
        o = self.Odds[0];
        print(type(o.Game))
        games = [o.Game for o in self.Odds]
        g = games[0]
        print(type(g))
        return [g['id'] for g in games]

    def GetDuplicateGameIDs(self):
        games = [o.Game for o in self.Odds]
        return [g['id'] for g, count in collections.Counter(games).items() if count > 1]

    def ParseResponse(self, response:str):
        try:
            obj = json.loads(response);
            return [Odds.fromDict(m) for m in obj] 
        except Exception as error:
            b = error;
            return None;