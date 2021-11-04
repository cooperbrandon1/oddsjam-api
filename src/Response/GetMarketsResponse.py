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
        try:
            obj = json.loads(response);
            return [Market.fromDict(m) for m in obj];
        except Exception as ex:
            return ex;