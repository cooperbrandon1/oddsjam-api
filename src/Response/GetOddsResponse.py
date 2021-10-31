#region Imports
import json;
from Models import Odds
from Base import ResponseBase;
#endregion Imports

class GetOddsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        self.Odds = self.ParseResponse(response);

    def GetPrices(self):
        '''Returns all prices in the response'''
        return [o.Price for o in self.Odds]

    def ParseResponse(self, response:str):
        try:
            obj = json.loads(response);
            return [Odds.fromDict(m) for m in obj] 
        except Exception as error:
            b = error;
            return None;