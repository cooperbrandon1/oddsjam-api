#region Imports
import Base;
import Request;
import Response;
import requests;
import datetime;
#endregion Imports

class OddsJamClient():
    def __init__(self,APIKEY:str):
        self.APIKEY = APIKEY;
        self.BaseUrl = 'https://api-external.oddsjam.com/api/feed'
    
    def SendRequest(self, request: Base.RequestBase):
        return requests.get(self.BaseUrl + request.ApiPath() + '?key=' + self.APIKEY, request.__dict__).text;

    #region Leagues
    def GetLeagues(self, sport: str = None, isLive: bool = None) -> Response.GetLeaguesResponse:
        '''Call Games endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetLeaguesResponse 
        Functions in response: GetLeagueNames()
        '''
        resp = self.SendRequest(Request.GetLeaguesRequest(sport, isLive));
        return Response.GetLeaguesResponse(resp);
    #endregion Leagues

    #region Games
    def GetGames(self, page: int = None, sport: str = None, league: str = None, isLive: bool = None, 
    startDateBefore: str = None, startDateAfter: str = None) -> Response.GetGamesResponse:
        '''Call Games endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetGamesResponse 
        Functions in response: GetGameIDs()
        '''
        resp = self.SendRequest(Request.GetGamesRequest(page, sport, league, isLive, startDateBefore, startDateAfter=startDateAfter)); 
        return Response.GetGamesResponse(resp);
    #endregion Games

    #region Markets
    def GetMarkets(self, page: int = None, gameId: int = None, isLive: bool = None) -> Response.GetMarketsResponse:
        '''Call Markets endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetMarketsResponse 
        Functions in response: GetMarketNames()
        '''
        resp = self.SendRequest(Request.GetMarketsRequest(page, gameId, isLive));
        return Response.GetMarketsResponse(resp);
    #endregion Markets

    #region Odds
    def GetOdds(self, page: int = None, sportsbook: str = None, marketName: str = None, sport: str = None, 
    league: str = None, gameId: int = None, isLive: bool = None, startDateBefore: datetime = None, startDateAfter: datetime = None) -> Response.GetOddsResponse:
        '''Call Odds endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetOddsResponse
        Functions in response: GetPrices()
        '''
        resp = self.SendRequest(Request.GetOddsRequest(page, sportsbook, marketName, sport, league, gameId, isLive, startDateBefore, startDateAfter));
        return Response.GetOddsResponse(resp);

    #endregion Odds

    #region Futures
    def GetFutures(self, page: int = None, sport: str = None, league: str = None) -> Response.GetFuturesResponse:
        resp = self.SendRequest(Request.GetFuturesRequest(page, sport, league));
        return Response.GetFuturesResponse(resp);
    #endregion Futures

    #region Future Odds
    def GetFutureOdds(self, page: int = None, sportsBook: str = None, 
    futureName: str = None, sport: str = None, league: str = None, futureId: int = None) -> Response.GetFutureOddsResponse:
        resp = self.SendRequest(Request.GetFutureOddsRequest(page, sportsBook, futureName, sport, league, futureId));
        return Response.GetFutureOddsResponse(resp);
    #endregion Future Odds

    #region Scores
    def GetScores(self, page: int = None, sport: str = None, league: str = None) -> Response.GetScoresResponse:
        resp = self.SendRequest(Request.GetScoresRequest(page, sport, league));
        return Response.GetScoresResponse(resp);
    #endregion Scores