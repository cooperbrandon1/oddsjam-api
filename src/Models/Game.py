#region Imports
from Base.ModelBase import ModelBase;
from Enum.SportsEnum import SportsEnum;
#endregion Imports

class Game(ModelBase):
    def __init__(cls,id = int, sport = SportsEnum, league = str, start_date = str, away_team = str, home_team = str, is_live = bool):
        cls._id = id;
        cls._sport = sport;
        cls._league = league;
        cls._startDate = start_date;
        cls._awayTeam = away_team;
        cls._homeTeam = home_team;
        cls._isLive = is_live;

    @property
    def ID(cls):
        return cls._id;

    @ID.setter
    def ID(cls, newId):
        cls._id = newId;

    @property
    def Sport(cls):
        return cls._sport;

    @Sport.setter
    def Sport(cls, newSport):
        cls._sport = newSport;

    @property
    def League(cls):
        return cls._league;

    @League.setter
    def League(cls, newLeague):
        cls._league = newLeague;

    @property
    def StartDate(cls):
        return cls._startDate;

    @StartDate.setter
    def StartDate(cls, newStartDate):
        cls._startDate = newStartDate;

    @property
    def AwayTeam(cls):
        return cls._awayTeam;

    @AwayTeam.setter
    def AwayTeam(cls, newAwayTeam):
        cls._awayTeam = newAwayTeam;

    @property
    def HomeTeam(cls):
        return cls._homeTeam;

    @HomeTeam.setter
    def HomeTeam(cls, newHomeTeam):
        cls._homeTeam = newHomeTeam;

    @property
    def IsLive(cls):
        return cls._isLive;
    
    @IsLive.setter
    def IsLive(cls, newIsLive):
        cls._isLive = newIsLive;

    