#region Imports
from Base import RequestBase;
from dataclasses import dataclass;
from typing import Literal;
#endregion Imports

@dataclass
class GetFuturesRequest(RequestBase):
    page: int = None;
    sport: str = None;
    league: str = None;
    
    def ApiPath(cls) -> str:
        return 'feed/futures';