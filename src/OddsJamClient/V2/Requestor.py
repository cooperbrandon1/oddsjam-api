from argparse import ArgumentError
import Request.V2;
import Response.V2;
import Base;
import datetime;

class v2Requestor:

    #region Leagues
    def GetLeagues(self, sport: str = None, isLive: bool = None) -> Response.V2.GetLeaguesResponse:
        '''Call Games endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetLeaguesResponse 
        Functions in response: GetLeagueNames()
        '''
        resp = self.SendRequest(Request.V2.GetLeaguesRequest(sport, isLive));
        return Response.V2.GetLeaguesResponse(resp);
    #endregion Leagues

    #region Games
    def GetGames(self, page: int = None, sport: str = None, league: str = None, isLive: bool = None, 
    startDateBefore: str = None, startDateAfter: str = None) -> Response.V2.GetGamesResponse:
        '''Call Games endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetGamesResponse 
        Functions in response: GetGameIDs()
        '''
        resp = self.SendRequest(Request.V2.GetGamesRequest(page, sport, league, isLive, startDateBefore, startDateAfter=startDateAfter)); 
        return Response.V2.GetGamesResponse(resp);
    #endregion Games

    #region Markets
    def GetMarkets(self, page: int = None, gameId: int = None, isLive: bool = None) -> Response.V2.GetMarketsResponse:
        '''Call Markets endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetMarketsResponse 
        Functions in response: GetMarketNames()
        '''
        resp = self.SendRequest(Request.V2.GetMarketsRequest(page, gameId, isLive));
        return Response.V2.GetMarketsResponse(resp);
    #endregion Markets

    #region Odds
    def GetOdds(self, sport: str = None, league: str = None, sportsbook: str = None, market_name: str = None, game_id: str = None, is_main: bool = None,
        is_live: bool = None, start_date_before: str = None, start_date_after: str = None) -> Response.V2.GetOddsResponse:
        '''Call Odds endpoint of OddsJam API.
        Required Parameters: None
        Returns: GetOddsResponse
        Functions in response: GetPrices()
        '''
        if all(v is None for v in [sport, league, sportsbook, market_name, game_id, is_main, is_live, start_date_before, start_date_after]):
            raise Base.InvalidGetOddsV2Error();
        resp = self.SendRequest(Request.V2.GetOddsRequest(sport, league, sportsbook, market_name, game_id, is_main, is_live, start_date_before, start_date_after));
        return Response.V2.GetOddsResponse(resp);

    #endregion Odds

    #region Futures
    def GetFutures(self, page: int = None, sport: str = None, league: str = None) -> Response.V2.GetFuturesResponse:
        resp = self.SendRequest(Request.V2.GetFuturesRequest(page, sport, league));
        return Response.V2.GetFuturesResponse(resp);
    #endregion Futures

    #region Future Odds
    def GetFutureOdds(self, page: int = None, sportsBook: str = None, 
    futureName: str = None, sport: str = None, league: str = None, futureId: int = None) -> Response.V2.GetFutureOddsResponse:
        resp = self.SendRequest(Request.V2.GetFutureOddsRequest(page, sportsBook, futureName, sport, league, futureId));
        return Response.V2.GetFutureOddsResponse(resp);
    #endregion Future Odds

    #region Scores
    def GetScores(self, page: int = None, sport: str = None, league: str = None) -> Response.V2.GetScoresResponse:
        resp = self.SendRequest(Request.V2.GetScoresRequest(page, sport, league));
        return Response.V2.GetScoresResponse(resp);
    #endregion Scores
