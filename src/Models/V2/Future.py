#region Imports
from Base import ModelBase;
from dataclasses import dataclass
#endregion Imports

@dataclass
class Future(ModelBase):
    id: str = None;
    sport: str = None;
    league: str = None;
    name: str = None;