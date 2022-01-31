import Request.V1;
import Response.V1;
import datetime;

class v1Requestor:

    #region Leagues
    def GetLeagues(self, sport: str = None, isLive: bool = None) -> Response.V1.GetLeaguesResponse:
        '''Call Games endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetLeaguesResponse 
        Functions in response: GetLeagueNames()
        '''
        resp = self.SendRequest(Request.V1.GetLeaguesRequest(sport, isLive));
        return Response.V1.GetLeaguesResponse(resp);
    #endregion Leagues

    #region Games
    def GetGames(self, page: int = None, sport: str = None, league: str = None, isLive: bool = None, 
    startDateBefore: str = None, startDateAfter: str = None) -> Response.V1.GetGamesResponse:
        '''Call Games endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetGamesResponse 
        Functions in response: GetGameIDs()
        '''
        resp = self.SendRequest(Request.V1.GetGamesRequest(page, sport, league, isLive, startDateBefore, startDateAfter=startDateAfter)); 
        return Response.V1.GetGamesResponse(resp);
    #endregion Games

    #region Markets
    def GetMarkets(self, page: int = None, gameId: int = None, isLive: bool = None) -> Response.V1.GetMarketsResponse:
        '''Call Markets endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetMarketsResponse 
        Functions in response: GetMarketNames()
        '''
        resp = self.SendRequest(Request.V1.GetMarketsRequest(page, gameId, isLive));
        return Response.V1.GetMarketsResponse(resp);
    #endregion Markets

    #region Odds
    def GetOdds(self, page: int = None, sportsbook: str = None, marketName: str = None, sport: str = None, 
    league: str = None, gameId: int = None, isLive: bool = None, startDateBefore: datetime = None, startDateAfter: datetime = None) -> Response.V1.GetOddsResponse:
        '''Call Odds endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetOddsResponse
        Functions in response: GetPrices()
        '''
        resp = self.SendRequest(Request.V1.GetOddsRequest(page, sportsbook, marketName, sport, league, gameId, isLive, startDateBefore, startDateAfter));
        return Response.V1.GetOddsResponse(resp);

    #endregion Odds

    #region Futures
    def GetFutures(self, page: int = None, sport: str = None, league: str = None) -> Response.V1.GetFuturesResponse:
        resp = self.SendRequest(Request.V1.GetFuturesRequest(page, sport, league));
        return Response.V1.GetFuturesResponse(resp);
    #endregion Futures

    #region Future Odds
    def GetFutureOdds(self, page: int = None, sportsBook: str = None, 
    futureName: str = None, sport: str = None, league: str = None, futureId: int = None) -> Response.V1.GetFutureOddsResponse:
        resp = self.SendRequest(Request.V1.GetFutureOddsRequest(page, sportsBook, futureName, sport, league, futureId));
        return Response.V1.GetFutureOddsResponse(resp);
    #endregion Future Odds

    #region Scores
    def GetScores(self, page: int = None, sport: str = None, league: str = None) -> Response.V1.GetScoresResponse:
        resp = self.SendRequest(Request.V1.GetScoresRequest(page, sport, league));
        return Response.V1.GetScoresResponse(resp);
    #endregion Scores
