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
        
    def ParseResponse(self, response:str):
        try:
            obj = json.loads(response);
            return [Odds.fromDict(m) for m in obj] 
        except Exception as ex:
            return ex;