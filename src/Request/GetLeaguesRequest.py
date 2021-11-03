#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
from Enum.SportsEnum import SportsEnum;
#endregion Imports

@dataclass
class GetLeaguesRequest(RequestBase):
    Sport: SportsEnum = None;
    IsLive: bool = None;

    def __post_init__(self):
        self.ApiPath = '/leagues';
        super().__init__();