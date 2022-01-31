#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
from typing import Literal;
#endregion Imports

@dataclass
class GetLeaguesRequest(RequestBase):
    sport: str = None;
    isLive: bool = None;

    def ApiPath(cls) -> str:
        return 'v2/leagues';