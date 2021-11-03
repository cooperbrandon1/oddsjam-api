#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
from Enum.SportsEnum import SportsEnum;
#endregion Imports

@dataclass
class GetLeaguesRequest(RequestBase):
    Sport: SportsEnum = None;
    IsLive: bool = None;
    ApiPath: str = '/leagues';