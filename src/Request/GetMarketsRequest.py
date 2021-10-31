#region Imports
from Base.RequestBase import RequestBase;
#endregion Imports

class GetMarketsRequest(RequestBase):
    def __init__(self, page: int = None, gameId: int = None, isLive: bool = None):
        super().__init__();
        self.Page = page;
        self.GameId = gameId;
        self.IsLive = isLive;
        self.ApiPath = '/markets';