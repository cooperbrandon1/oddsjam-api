#region Imports
from Base import ModelBase;
from dataclasses import dataclass;
from Models.V1 import Future;
#endregion Imports

@dataclass
class FutureOdds(ModelBase):
    future: Future = None;
    sports_book: str = None;
    name: str = None;
    price: float = None;
    checked_date: str = None;
    changed_date: str = None;