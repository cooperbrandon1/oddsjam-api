#region Imports
from Base import RequestBase;
from Enum import SportsEnum;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class GetFuturesRequest(RequestBase):
    Page: int = None;
    Sport: SportsEnum = None;
    League: str = None;
    ApiPath: str = '/futures';