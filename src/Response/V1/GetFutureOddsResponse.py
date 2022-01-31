#region Imports
import json;
from Models.V1 import FutureOdds, Future;
from Base import ResponseBase;
#endregion Imports

class GetFutureOddsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        self.FutureOdds = self.ParseResponse(response);
        
    def ParseResponse(self, response:str):
        try:
            obj = json.loads(response);
            futureOdds = [FutureOdds.fromDict(m) for m in obj]; 
            for f in futureOdds:
                f.future = Future.fromDict(f.future);
                f.sports_book = f.sports_book['name'];
            return futureOdds;
        except Exception as ex:
            return ex;