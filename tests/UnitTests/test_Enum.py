#region Imports
import sys
sys.path.append('././src');
import Enum;
import unittest;
import Base;
from dataclasses import dataclass;
#endregion Imports

@dataclass
class TestObject:
    sport: Enum.SportsEnum = None
    sportsBook: Enum.SportsBooksEnum = None

    def __post_init__(self):
        Base.EnforceTypes(self);

class test_Enums(unittest.TestCase):

    #region Sports
    def test_ValidSportEnum_ShouldReturnSuccess(self):
        testObj = TestObject(Enum.SportsEnum.football);

    def test_ValidSportEnum_ShouldReturnSuccess(self):
        testObj = TestObject(sport='football');

    def test_InvalidSportEnum_ShouldReturnSuccess(self):
        with(self.assertRaises(ValueError)):
            testObj = TestObject('curling');
    #endregion Sports

    #region SportsBooks
    def test_ValidSportEnum_ShouldReturnSuccess(self):
        testObj = TestObject(Enum.SportsBooksEnum.BetMGM);

    def test_ValidSportEnum_ShouldReturnSuccess(self):
        testObj = TestObject(sportsBook='betmgm');
        print(testObj.sportsBook.value);

    def test_InvalidSportEnum_ShouldReturnSuccess(self):
        with(self.assertRaises(ValueError)):
            testObj = TestObject('1-800 Bet');
    #endregion Sports
    
    def Run(self):
        unittest.main();