#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
#endregion Imports

@dataclass
class GetMarketsRequest(RequestBase):
    Page: int = None;
    GameId: int = None;
    IsLive: bool = None;

    def __post_init__(self):
        self.ApiPath = '/markets';
        super().__init__();