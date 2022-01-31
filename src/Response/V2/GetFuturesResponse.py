#region Imports
import json;
from Models.V2 import Future;
from Base import ResponseBase;
#endregion Imports

class GetFuturesResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        resp = json.loads(response);
        obj = self.ParseResponse(json.dumps(resp['data']));
        self.Futures = [f for f in obj]
        
    def ParseResponse(self, response:str):
        try:
            return json.loads(response, object_hook=lambda d: Future(**d));
        except Exception as ex:
            return ex;