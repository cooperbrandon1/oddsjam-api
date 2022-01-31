#region Imports
import json;
from Models.V2 import Game;
from Base import ResponseBase;
#endregion Imports

class GetGamesResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        resp = json.loads(response);
        obj = self.ParseResponse(json.dumps(resp['data']));
        self.Games = [g for g in obj]

    def ParseResponse(self, response:str):
        try:
            return json.loads(response, object_hook=lambda d: Game(**d));
        except Exception as ex:
            return ex;