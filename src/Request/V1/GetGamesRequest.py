#region Imports
from Base import RequestBase;
from typing import Literal;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class GetGamesRequest(RequestBase):
    page: int = None;
    sport: str = None;
    league: str = None;
    isLive: bool = None;
    startDateBefore: str = None;
    startDateAfter: str = None;
    
    def ApiPath(cls) -> str:
        return 'feed/games';

    def __post_init__(cls):
        return super().__post_init__()