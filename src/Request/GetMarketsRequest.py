#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
#endregion Imports

@dataclass
class GetMarketsRequest(RequestBase):
    Page: int = None;
    GameId: int = None;
    IsLive: bool = None;
    ApiPath: str = '/markets';