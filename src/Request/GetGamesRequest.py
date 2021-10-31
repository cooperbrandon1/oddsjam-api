#region Imports
from Base import RequestBase;
from Enum import SportsEnum;
#endregion Imports

class GetGamesRequest(RequestBase):
    def __init__(self, page: int = None, sport: SportsEnum = None, league: str = None, isLive: bool = None, startDateBefore: str = None, startDateAfter: str = None):
        super().__init__();
        self.Page = page;
        self.Sport = sport;
        self.IsLive = isLive;
        self.League = league;
        self.StartDateBefore = startDateBefore;
        self.StartDateAfter = startDateAfter;
        self.ApiPath = '/games';