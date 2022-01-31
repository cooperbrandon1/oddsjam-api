#region Imports
from Base import ModelBase;
from dataclasses import dataclass;
from typing import List
#endregion Imports

@dataclass
class FutureOdd(ModelBase):
    id: str = None;
    sports_book_name: str = None;
    name: str = None;
    price: float = None;
    checked_date: str = None;

@dataclass
class FutureOdds(ModelBase):
    id: int = None;
    name: str = None;
    sport: str = None;
    league: float = None;
    odds: List[FutureOdd] = None;

