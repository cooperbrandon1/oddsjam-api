#region Imports
from Base import ModelBase;
from Models.V2 import Game;
from datetime import datetime;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class Score(ModelBase):
    game: Game = None;
    period_scores: list = None;
    season_type: str = None;
    season_week: str = None;
    description: str = None;
    venue_name: str = None;
    venue_location: str = None;
    status: str = None;
    period: str = None;
    clock: str = None;
    last_play: str = None;
    home_final_score: int = None;
    away_final_score: int = None;
    checked_date: datetime = None;
    changed_date: datetime = None;