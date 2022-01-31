#region Imports
from __future__ import annotations;
import Base;
import requests;
from OddsJamClient.V1 import v1Requestor;
from OddsJamClient.V2 import v2Requestor;
import types;
#endregion Imports

class OddsJamClient():
    def __init__(self,APIKEY:str):
        self.APIKEY = APIKEY;
        self.BaseUrl = 'https://api-external.oddsjam.com/api/';
        self.V1Requestor = v1Requestor;
        self.V2Requestor = v2Requestor;
        self.UseV1();

    def UseV1(self):
        self.Version = 1;
        self.GetFutureOdds = types.MethodType(v1Requestor.GetFutureOdds, self);
        self.GetFutures = types.MethodType(v1Requestor.GetFutures, self);
        self.GetGames = types.MethodType(v1Requestor.GetGames, self);
        self.GetLeagues = types.MethodType(v1Requestor.GetLeagues, self);
        # self.GetMarkets = types.MethodType(v1Requestor.GetMarkets, self);
        self.GetOdds = types.MethodType(v1Requestor.GetOdds, self);
        self.GetScores = types.MethodType(v1Requestor.GetScores, self);
    
    def UseV2(self):
        self.Version = 2;
        self.GetFutureOdds = types.MethodType(v2Requestor.GetFutureOdds, self);
        self.GetFutures = types.MethodType(v2Requestor.GetFutures, self);
        self.GetGames = types.MethodType(v2Requestor.GetGames, self);
        self.GetLeagues = types.MethodType(v2Requestor.GetLeagues, self);
        self.GetMarkets = types.MethodType(v2Requestor.GetMarkets, self);
        self.GetOdds = types.MethodType(v2Requestor.GetOdds, self);
        self.GetScores = types.MethodType(v2Requestor.GetScores, self);

    def SendRequest(self, request: Base.RequestBase):
        return requests.get(self.BaseUrl + request.ApiPath() + '?key=' + self.APIKEY, request.__dict__).text;

    