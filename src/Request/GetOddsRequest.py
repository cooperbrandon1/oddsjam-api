#region Imports
import datetime;
from Base.RequestBase import RequestBase;
from Enum.SportsEnum import SportsEnum;
from Enum.SportsBooksEnum import SportsBooksEnum;
#endregion Imports

class GetOddsRequest(RequestBase):
    def __init__(self, page: int = None, sportsbook: SportsBooksEnum = None, marketName: str = None, sport: SportsEnum = None, 
    league: str = None, gameId: int = None, isLive: bool = None, startDateBefore: datetime = None, startDateAfter: datetime = None):
        super().__init__();
        self.Page = page;
        self.SportsBook = sportsbook;
        self.MarketName = marketName;
        self.Sport = sport;
        self.League = league;
        self.GameId = gameId;
        self.IsLive = isLive;
        self.StartDateBefore = startDateBefore;
        self.StartDateAfter = startDateAfter;
        self.ApiPath = '';