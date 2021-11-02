#region Imports
import datetime;
from dataclasses import dataclass;
from Base.RequestBase import RequestBase;
from Enum.SportsEnum import SportsEnum;
from Enum.SportsBooksEnum import SportsBooksEnum
#endregion Imports

@dataclass
class GetOddsRequest(RequestBase):
    Page: int = None;
    SportsBook: SportsBooksEnum = None
    MarketName: str = None
    Sport: SportsEnum = None
    League: str = None
    GameId: int = None
    IsLive: bool = None
    StartDateBefore: str = None
    StartDateAfter: str = None

    def __post_init__(self):
        self.ApiPath = '';
        super().__init__();