#region Imports
import json;
from Base import ResponseBase;
from Models import Market;
#endregion Imports

class GetMarketsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        self.Markets = self.ParseResponse(response);

    def ParseResponse(self, response: str):
        obj = json.loads(response);
        return [Market.fromDict(m) for m in obj] 

    def GetMarketNames(self):
        '''Returns all market names in the response'''
        return [m.Name for m in self.Markets];