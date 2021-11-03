#region Imports
from Base import ModelBase;
from Enum import SportsBooksEnum, SportsEnum;
from dataclasses import dataclass;
from Models import Future;
#endregion Imports

@dataclass
class FutureOdds(ModelBase):
    future: Future = None;
    sports_book: SportsBooksEnum = None;
    name: str = None;
    price: SportsEnum = None;
    checked_date: str = None;
    changed_date: str = None;