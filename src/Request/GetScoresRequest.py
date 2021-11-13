#region Imports
from dataclasses import dataclass;
from Base import RequestBase;
from Enum.SportsEnum import SportsEnum;
#endregion Imports

@dataclass
class GetScoresRequest(RequestBase):
    Page: int = None;
    Sport: SportsEnum = None;
    League: str = None;
    ApiPath: str = '/scores';