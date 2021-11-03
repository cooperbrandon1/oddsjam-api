#region Imports
from Base import RequestBase;
from Enum import SportsBooksEnum;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class GetFutureOddsRequest(RequestBase):
    Page: int = None;
    SportsBook: SportsBooksEnum = None;
    League: str = None;
    ApiPath: str = '/future-odds';