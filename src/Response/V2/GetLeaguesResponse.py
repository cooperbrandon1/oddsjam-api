#region Imports
import json;
from Base import ResponseBase;
from Models.V2 import League;
#endregion Imports

class GetLeaguesResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        self.Leagues = self.ParseResponse(self.RawResponse);
    
    def ParseResponse(self, response: str):
        try:
            responseObj = json.loads(response);
            return [League(l) for l in responseObj['data']];
        except Exception as ex:
            return ex;