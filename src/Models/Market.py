#region Imports
from Base import ModelBase;
from Models.Game import Game;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class Market(ModelBase):
    Game: Game = None;
    Name: str = None;