#region Imports
import sys
import unittest;
sys.path.append('././src');
import Request;
import Enum;
#endregion Imports

class test_Requests(unittest.TestCase):

    #region GetGamesRequest
    def test_GetGamesRequest_NoArgs_ShouldReturnSuccess(self):
        request = Request.GetGamesRequest();
        self.assertIsInstance(request, Request.GetGamesRequest);

    def test_GetGamesRequest_ValidArgs_ShouldReturnSuccess(self):
        request = Request.GetGamesRequest(Page=1);
        self.assertIsInstance(request, Request.GetGamesRequest);

    def test_GetGamesRequest_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            request = Request.GetGamesRequest(Page='1');
    #endregion GetGamesRequest
    
    #region GetLeaguesRequest
    def test_GetLeaguesRequest_NoArgs_ShouldReturnSuccess(self):
        request = Request.GetLeaguesRequest();
        self.assertIsInstance(request, Request.GetLeaguesRequest);

    def test_GetLeaguesRequest_ValidArgs_ShouldReturnSuccess(self):
        request = Request.GetLeaguesRequest(Sport=Enum.SportsEnum.football);
        self.assertIsInstance(request, Request.GetLeaguesRequest);

    def test_GetLeaguesRequest_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            request = Request.GetLeaguesRequest(IsLive='123');

    def test_GetLeaguesRequest_InvalidSport_ShouldReturnValueError(self):
        with self.assertRaises(TypeError):
            request = Request.GetLeaguesRequest(Sport=123);
    #endregion GetLeaguesRequest
    
    #region GetMarketsRequest
    def test_GetMarketsRequest_NoArgs_ShouldReturnSuccess(self):
        request = Request.GetMarketsRequest();
        self.assertIsInstance(request, Request.GetMarketsRequest);

    def test_GetMarketsRequest_ValidArgs_ShouldReturnSuccess(self):
        request = Request.GetMarketsRequest(Page=1);
        self.assertIsInstance(request, Request.GetMarketsRequest);

    def test_GetMarketsRequest_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            request = Request.GetMarketsRequest(Page='1');
    #endregion GetMarketsRequest
    
    #region GetOddsRequest
    def test_GetOddsRequest_NoArgs_ShouldReturnSuccess(self):
        request = Request.GetOddsRequest();
        self.assertIsInstance(request, Request.GetOddsRequest);

    def test_GetOddsRequest_ValidArgs_ShouldReturnSuccess(self):
        request = Request.GetOddsRequest(Page=1);
        self.assertIsInstance(request, Request.GetOddsRequest);

    def test_GetOddsRequest_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            request = Request.GetOddsRequest(Page='1');
    #endregion GetOddsRequest

    #region GetFuturesRequest
    def test_GetFuturesRequest_NoArgs_ShouldReturnSuccess(self):
        request = Request.GetFuturesRequest();
        self.assertIsInstance(request, Request.GetFuturesRequest);

    def test_GetFuturesRequest_ValidArgs_ShouldReturnSuccess(self):
        request = Request.GetFuturesRequest(Page=1);
        self.assertIsInstance(request, Request.GetFuturesRequest);

    def test_GetFuturesRequest_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            request = Request.GetFuturesRequest(Page='1');

    def test_GetFuturesRequest_InvalidSport_ShouldReturnValueError(self):
        with self.assertRaises(TypeError):
            request = Request.GetFuturesRequest(Sport=123);
    #endregion GetFuturesRequest

    #region GetFutureOddsRequest
    def test_GetFutureOddsRequest_NoArgs_ShouldReturnSuccess(self):
        request = Request.GetFutureOddsRequest();
        self.assertIsInstance(request, Request.GetFutureOddsRequest);

    def test_GetFutureOddsRequest_ValidArgs_ShouldReturnSuccess(self):
        request = Request.GetFutureOddsRequest(Page=1);
        self.assertIsInstance(request, Request.GetFutureOddsRequest);

    def test_GetFutureOddsRequest_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            request = Request.GetFutureOddsRequest(Page='1');

    def test_GetFutureOddsRequest_InvalidSportsBook_ShouldReturnValueError(self):
        with self.assertRaises(TypeError):
            request = Request.GetFutureOddsRequest(SportsBook=123);
    #endregion GetFutureOddsRequest

if __name__=='__main__':
    unittest.main();