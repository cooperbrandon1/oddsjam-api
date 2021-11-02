#region Imports
from Base.ModelBase import ModelBase
from Models.Game import Game;
#endregion Imports

class Market(ModelBase):
    def __init__(cls,game: Game = None, name: str = None):
        cls._game = game;
        cls._name = name;

    @property
    def Game(cls):
        return cls._game;
    
    @Game.setter
    def Game(cls, newGame: Game):
        cls._game = newGame;

    @property
    def Name(cls):
        return cls._name;

    @Name.setter
    def Name(cls, newName: str):
        cls._name = newName;