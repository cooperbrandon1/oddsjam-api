#region Imports
from Base.RequestBase import RequestBase;
from Enum.SportsEnum import SportsEnum;
#endregion Imports

class GetLeaguesRequest(RequestBase):
    def __init__(self, sport: SportsEnum = None, isLive: bool = None):
        super().__init__();
        self.Sport = sport;
        self.IsLive = isLive;
        self.ApiPath = '/leagues';