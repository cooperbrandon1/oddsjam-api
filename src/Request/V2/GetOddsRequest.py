#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
#endregion Imports

@dataclass
class GetOddsRequest(RequestBase):
    sport: str = None
    league: str = None
    sportsbook: str = None
    market_name: str = None
    game_id: str = None
    is_main: bool = None
    is_live: bool = None
    start_date_before: str = None
    start_date_after: str = None

    def ApiPath(cls) -> str:
        return 'v2/game-odds';