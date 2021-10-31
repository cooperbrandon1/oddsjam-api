#region Imports
from Base.ModelBase import ModelBase;
from Enum.SportsEnum import SportsEnum;
#endregion Imports

class Game(ModelBase):
    def __init__(self,id = int, sport = SportsEnum, league = str, start_date = str, away_team = str, home_team = str, is_live = bool):
        self.ID = id;
        self.Sport = sport;
        self.League = league;
        self.StartDate = start_date;
        self.AwayTeam = away_team;
        self.HomeTeam = home_team;
        self.IsLive = is_live;