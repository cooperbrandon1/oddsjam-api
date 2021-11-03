#region Imports
import json;
from Models import FutureOdds;
from Base import ResponseBase;
#endregion Imports

class GetFutureOddsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        b = json.loads(response);
        obj = self.ParseResponse(response);
        self.FutureOdds = [f for f in obj]
        
    def ParseResponse(self, response:str):
        try:
            obj = json.loads(response);
            return [FutureOdds.fromDict(m) for m in obj] 
        except Exception as ex:
            return None;