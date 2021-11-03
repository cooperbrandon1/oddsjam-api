#region Imports
from Base import ModelBase;
from Models import Game;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class Market(ModelBase):
    game: Game = None;
    name: str = None;