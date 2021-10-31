#region Imports
from Base.ModelBase import ModelBase
from Models.Game import Game;
#endregion Imports

class Market(ModelBase):
    def __init__(self,game: Game = None, name: str = None):
        self._game = game;
        self._name = name;

    @property
    def Game(self):
        return self._game;
    
    @Game.setter
    def Game(self, newGame: Game):
        self._game = newGame;

    @property
    def Name(self):
        return self._name;

    @Name.setter
    def Name(self, newName: str):
        self._name = newName;