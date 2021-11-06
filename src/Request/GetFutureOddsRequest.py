#region Imports
from Base import RequestBase;
from Enum import SportsBooksEnum;
from dataclasses import dataclass

from Enum.SportsEnum import SportsEnum;
#endregion Imports

@dataclass
class GetFutureOddsRequest(RequestBase):
    Page: int = None;
    SportsBook: SportsBooksEnum = None;
    FutureName: str = None;
    Sport: SportsEnum = None;
    League: str = None;
    FutureID: int = None;
    ApiPath: str = '/future-odds';