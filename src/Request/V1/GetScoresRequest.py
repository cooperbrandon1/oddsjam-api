#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
#endregion Imports

@dataclass
class GetScoresRequest(RequestBase):
    page: int = None;
    sport: str = None;
    league: str = None;

    def ApiPath(cls) -> str:
        return 'feed/scores';