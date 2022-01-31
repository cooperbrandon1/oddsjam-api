#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
#endregion Imports

@dataclass
class GetMarketsRequest(RequestBase):
    page: int = None;
    gameId: int = None;
    isLive: bool = None;

    def ApiPath(cls) -> str:
        return 'v2/markets';