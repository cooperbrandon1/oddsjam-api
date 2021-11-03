#region Imports
from Base import RequestBase;
from Enum import SportsEnum;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class GetGamesRequest(RequestBase):
    Page: int = None;
    Sport: SportsEnum = None;
    IsLive: bool = None;
    League: str = None;
    StartDateBefore: str = None;
    StartDateAfter: str = None;
    ApiPath: str = '/games';