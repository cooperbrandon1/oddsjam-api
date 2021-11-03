#region Imports
import datetime;
from dataclasses import dataclass;
from Enum import SportsBooksEnum;
from Models import Game;
from Base import ModelBase;
#endregion Imports

@dataclass
class Odds(ModelBase):
    game: Game = None
    market_name: str = None
    sports_book: SportsBooksEnum = None
    name: str = None
    price: float = None
    is_main: bool = None
    is_live: bool = None
    checked_date: datetime = None
    changed_date: datetime = None