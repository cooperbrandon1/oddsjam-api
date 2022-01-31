#region Imports
import json;
from Models.V2 import FutureOdds, FutureOdd;
from Base import ResponseBase;
#endregion Imports

class GetFutureOddsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        resp = json.loads(response);
        self.FutureOdds = self.ParseResponse(json.dumps(resp['data']));
        
    def ParseResponse(self, response:str):
        try:
            obj = json.loads(response);
            futureOdds = [FutureOdds.fromDict(m) for m in obj]; 
            for f in futureOdds:
                f.odds = [FutureOdd.fromDict(m) for m in f.odds]
            return futureOdds;
        except Exception as ex:
            return ex;