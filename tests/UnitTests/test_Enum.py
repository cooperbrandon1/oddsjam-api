#region Imports
import sys
sys.path.append('././src');
import Enum;
import unittest;
import Base;
from dataclasses import dataclass;
#endregion Imports

#region Test Model
@dataclass
class TestObject:
    sport: Enum.SportsEnum = None
    sportsBook: Enum.SportsBooksEnum = None

    def __post_init__(self):
        Base.EnforceTypes(self);
#endregion Test Model

class test_Enums(unittest.TestCase):

    #region Sports
    def test_ValidSportsEnum_ShouldReturnSuccess(self):
        testObj = TestObject(sport=Enum.SportsEnum.football);
        self.assertIsInstance(testObj, TestObject);

    def test_ValidSportsEnum_WithString_ShouldReturnSuccess(self):
        testObj = TestObject(sport='football');
        self.assertIsInstance(testObj, TestObject);

    def test_InvalidSportsEnum_ShouldReturnSuccess(self):
        with(self.assertRaises(ValueError)):
            testObj = TestObject('curling');
    #endregion Sports

    #region SportsBooks
    def test_ValidSportsBookEnum_ShouldReturnSuccess(self):
        testObj = TestObject(sportsBook=Enum.SportsBooksEnum.BetMGM);
        self.assertIsInstance(testObj, TestObject);

    def test_ValidSportsBookEnum_WithString_ShouldReturnSuccess(self):
        testObj = TestObject(sportsBook='betmgm');
        self.assertIsInstance(testObj, TestObject);

    def test_InvalidSportsBookEnum_ShouldReturnSuccess(self):
        with(self.assertRaises(ValueError)):
            testObj = TestObject('1-800 Bet');
    #endregion Sports
    
if __name__ == '__main__':
    unittest.main();