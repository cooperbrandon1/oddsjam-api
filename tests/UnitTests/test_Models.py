#region Imports
import sys
sys.path.append('././src');
from Enum.SportsEnum import SportsEnum;
import Models;
import unittest;
#endregion Imports

class test_Models(unittest.TestCase):

    #region Game
    def test_Game_NoArgs_ShouldReturnSuccess(self):
        model = Models.Game();
        self.assertIsInstance(model, Models.Game);
        
    def test_Game_ValidArgs_ShouldReturnSuccess(self):
        model = Models.Game(id=1);
        model = Models.Game(sport=SportsEnum.football);
        model = Models.Game(sport='football');
        self.assertIsInstance(model, Models.Game);
        
    def test_Game_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            model = Models.Game(id='1');
    #endregion Game
    
    #region League
    def test_League_NoArgs_ShouldReturnSuccess(self):
        model = Models.League();
        self.assertIsInstance(model, Models.League);
        
    def test_League_ValidArgs_ShouldReturnSuccess(self):
        model = Models.League(name='ncaa');
        self.assertIsInstance(model, Models.League);
        
    def test_League_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            model = Models.League(name=1234);
    #endregion League
    
    #region Market
    def test_Market_NoArgs_ShouldReturnSuccess(self):
        model = Models.Market();
        self.assertIsInstance(model, Models.Market);
        
    def test_Market_ValidArgs_ShouldReturnSuccess(self):
        model = Models.Market(name='MarketOne');
        self.assertIsInstance(model, Models.Market);
        
    def test_Market_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            model = Models.Market(name=1234);
    #endregion Market

    #region Odds
    def test_Odds_NoArgs_ShouldReturnSuccess(self):
        model = Models.Odds();
        self.assertIsInstance(model, Models.Odds);
        
    def test_Odds_ValidArgs_ShouldReturnSuccess(self):
        model = Models.Odds(name='TestName');
        self.assertIsInstance(model, Models.Odds);
        
    def test_Odds_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            model = Models.Odds(name=1234);
    #endregion Odds
    
    #region Futures
    def test_Futures_NoArgs_ShouldReturnSuccess(self):
        model = Models.Future();
        self.assertIsInstance(model, Models.Future);
        
    def test_Futures_ValidArgs_ShouldReturnSuccess(self):
        model = Models.Future(name='TestName');
        self.assertIsInstance(model, Models.Future);
        
    def test_Futures_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            model = Models.Future(name=1234);
    #endregion Futures
    
    #region FutureOdds
    def test_Futures_NoArgs_ShouldReturnSuccess(self):
        model = Models.FutureOdds();
        self.assertIsInstance(model, Models.FutureOdds);
        
    def test_Futures_ValidArgs_ShouldReturnSuccess(self):
        model = Models.FutureOdds(name='TestName');
        self.assertIsInstance(model, Models.FutureOdds);
        
    def test_Futures_InvalidArgs_ShouldReturnTypeError(self):
        with self.assertRaises(TypeError):
            model = Models.FutureOdds(name=1234);
    #endregion FutureOdds
    
if __name__ == '__main__':
    unittest.main();