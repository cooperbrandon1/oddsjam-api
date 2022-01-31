#region Imports
from Base import ModelBase;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class League(ModelBase):
    name: str = None;