#region Imports
from Base import RequestBase;
from typing import Literal;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class GetFutureOddsRequest(RequestBase):
    page: int = None;
    sportsbook: str = None;
    futureName: str = None;
    sport: str = None;
    league: str = None;
    futureID: int = None;

    def ApiPath(cls) -> str:
        return 'v2/future-odds';