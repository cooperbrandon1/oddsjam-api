#region Imports
import Enum;
import Base;
import Request;
import Response;
import requests;
import datetime;
#endregion Imports

class OddsJamClient():
    def __init__(self,APIKEY:str):
        #TODO - Move APIKey to one-time encrypt function - create token so user only has to make one call to use the API
        #e.g OddsJamClient.EncryptKey(APIKEY) -> write to ./Secrets/encoded_apikey -> refer to encoded_apikey for subsequent calls
        self.APIKEY = APIKEY;
        self.BaseUrl = 'https://api-external.oddsjam.com/api/feed'
    
    #Move this to separate builder?
    def BuildRequest(self, request: Base.RequestBase):
        return self.BaseUrl + request.ApiPath + '?key=' + self.APIKEY + request.GetArgString();

    #region Leagues
    def GetLeagues(self, sport: Enum.SportsEnum = None, isLive: bool = None) -> Response.GetLeaguesResponse:
        '''Call Games endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetLeaguesResponse 
        Functions in response: GetLeagueNames()
        '''
        request = self.BuildRequest(Request.GetLeaguesRequest(Sport=sport, IsLive=isLive));
        #Response type from API - List<League>
        response = self.HandleAPICall(request);
        return Response.GetLeaguesResponse(response.text);
    #endregion Leagues

    #region Games
    def GetGames(self, page: int = None, sport: Enum.SportsEnum = None, league: str = None, isLive: bool = None, 
    startDateBefore: str = None, startDateAfter: str = None) -> Response.GetGamesResponse:
        '''Call Games endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetGamesResponse 
        Functions in response: GetGameIDs()
        '''
        request = self.BuildRequest(Request.GetGamesRequest(Page=page,Sport=sport,League=league,IsLive=isLive,StartDateBefore=startDateBefore,
        StartDateAfter=startDateAfter)); 
        #Response type from API: List<Game>
        response = self.HandleAPICall(request);
        return Response.GetGamesResponse(response.text);
    #endregion Games

    #region Markets
    def GetMarkets(self, page: int = None, gameId: int = None, isLive: bool = None) -> Response.GetMarketsResponse:
        '''Call Markets endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetMarketsResponse 
        Functions in response: GetMarketNames()
        '''
        request = self.BuildRequest(Request.GetMarketsRequest(page, gameId, isLive));
        #Response type from API: Dict<Game,Name>
        response = self.HandleAPICall(request);
        return Response.GetMarketsResponse(response.text);
    #endregion Markets

    #region Odds
    def GetOdds(self, page: int = None, sportsbook: Enum.SportsBooksEnum = None, marketName: str = None, sport: Enum.SportsEnum = None, 
    league: str = None, gameId: int = None, isLive: bool = None, startDateBefore: datetime = None, startDateAfter: datetime = None) -> Response.GetOddsResponse:
        '''Call Odds endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetOddsResponse
        Functions in response: GetPrices()
        '''
        request = self.BuildRequest(Request.GetOddsRequest(Page=page, SportsBook=sportsbook, 
        MarketName=marketName, Sport=sport, League=league, GameId=gameId, IsLive=isLive, 
        StartDateBefore=startDateBefore, StartDateAfter=startDateAfter));
        response = self.HandleAPICall(request);
        return Response.GetOddsResponse(response.text);

    #endregion Odds

    #region Futures
    def GetFutures(self, page: int = None, sport: Enum.SportsEnum = None, league: str = None) -> Response.GetFuturesResponse:
        request = self.BuildRequest(Request.GetFuturesRequest(Page = page, Sport=sport, League=league));
        response = self.HandleAPICall(request);
        return Response.GetFuturesResponse(response.text);
    #endregion Futures

    #region Future Odds
    def GetFutureOdds(self, page: int = None, sportsBook: Enum.SportsBooksEnum = None, 
    futureName: str = None, sport: Enum.SportsEnum = None, league: str = None, futureId: int = None) -> Response.GetFutureOddsResponse:
        request = self.BuildRequest(Request.GetFutureOddsRequest(Page = page, SportsBook=sportsBook, FutureName=futureName, Sport=sport, League=league, FutureID = futureId));
        response = self.HandleAPICall(request);
        return Response.GetFutureOddsResponse(response.text);
    #endregion Future Odds

    #region Scores
    def GetScores(self, page: int = None, sport: Enum.SportsEnum = None, league: str = None) -> Response.GetScoresResponse:
        request = self.BuildRequest(Request.GetScoresRequest(Page = page, Sport=sport, League=league));
        response = self.HandleAPICall(request);
        return Response.GetScoresResponse(response.text);
    #endregion Scores
    
    #region API calls
    def HandleAPICall(self, request: requests.models.Request):
        #TODO - Properly log/return errors
        try:
            return self.HandleResponse(requests.get(request));
        except Exception as exc:
            print('error sending request');

    def HandleResponse(self, response: requests.models.Response):
        #TODO - Properly log/return errors
        if(response.status_code != 200):
            print('Invalid request')
            return None;
        return response;
    #endregion API calls