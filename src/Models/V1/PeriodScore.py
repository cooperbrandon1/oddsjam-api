#region Imports
from Base import ModelBase;
from dataclasses import dataclass
#endregion Imports

@dataclass
class PeriodScore(ModelBase):
    period_number: int = None;
    team: str = None;
    score: int = None;