#region Imports
import json;
from Base import ResponseBase;
from Models.V1 import Market, Game;
#endregion Imports

class GetMarketsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        self.Markets = self.ParseResponse(response);

    def ParseResponse(self, response: str):
        try:
            obj = json.loads(response);
            marketObjects = [Market.fromDict(m) for m in obj];
            for m in marketObjects:
                m.game = Game.fromDict(m.game);
            return marketObjects;
        except Exception as ex:
            return ex;