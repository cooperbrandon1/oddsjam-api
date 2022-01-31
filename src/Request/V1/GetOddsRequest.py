#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
#endregion Imports

@dataclass
class GetOddsRequest(RequestBase):
    page: int = None;
    sportsbook: str = None
    marketName: str = None
    sport: str = None;
    league: str = None
    gameId: int = None
    isLive: bool = None
    startDateBefore: str = None
    startDateAfter: str = None

    def ApiPath(cls) -> str:
        return 'feed/';