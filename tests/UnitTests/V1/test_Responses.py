#region Imports
import sys
import unittest;
sys.path.append('././src');
import Models, Response;
#also gross, clean this up
import os
absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
parentDirectory = os.path.dirname(fileDirectory)
dataPath = os.path.join(parentDirectory, 'TestData/')   
import json
from pandas import DataFrame
#endregion Imports

class test_Requests(unittest.TestCase):

    #region Setup
    def setUp(self) -> None:
        with(open(dataPath+'GetGamesResponse.json') as f):
            j = json.load(f);
            self.GamesResponseText =  json.dumps(j);
        with(open(dataPath+'GetFutureOddsResponse.json') as f):
            j = json.load(f);
            self.FutureOddsResponseText =  json.dumps(j);
        with(open(dataPath+'GetMarketsResponse.json') as f):
            j = json.load(f);
            self.MarketsResponseText =  json.dumps(j);
        with(open(dataPath+'GetOddsResponse.json') as f):
            j = json.load(f);
            self.OddsResponseText =  json.dumps(j);
        with(open(dataPath+'GetFuturesResponse.json') as f):
            j = json.load(f);
            self.FuturesResponseText =  json.dumps(j);
        with(open(dataPath+'GetFutureOddsResponse.json') as f):
            j = json.load(f);
            self.FutureOddsResponseText =  json.dumps(j);
        with(open(dataPath+'GetScoresResponse.json') as f):
            j = json.load(f);
            self.ScoresResponseText =  json.dumps(j);
    #endregion Setup
    
    #region GetGamesResponse
    def test_GetGamesResponse_Games_ShouldReturnSuccess(self):
        response = Response.GetGamesResponse(self.GamesResponseText);
        self.assertIsInstance(response, Response.GetGamesResponse);
        self.assertIsNotNone(response, response.Games);
    #endregion GetGamesResponse
    
    #region GetMarketsResponse
    def test_GetMarketsResponse_Markets_ShouldReturnSuccess(self):
        response = Response.GetMarketsResponse(self.MarketsResponseText);
        self.assertIsInstance(response, Response.GetMarketsResponse);
        self.assertIsNotNone(response, response.Markets);
        self.assertIsInstance(response.Markets[0].game, Models.Game);
    #endregion GetMarketsResponse
    
    #region GetOddsResponse
    def test_GetOddsResponse_Odds_ShouldReturnSuccess(self):
        response = Response.GetOddsResponse(self.OddsResponseText);
        self.assertIsInstance(response, Response.GetOddsResponse);
        self.assertIsNotNone(response, response.Odds);
        self.assertIsInstance(response.Odds[0].game, Models.Game);
    #endregion GetOddsResponse
    
    #region GetFutureResponse
    def test_GetFutureResponse_Futures_ShouldReturnSuccess(self):
        response = Response.GetFuturesResponse(self.FuturesResponseText);
        self.assertIsInstance(response, Response.GetFuturesResponse);
        self.assertIsNotNone(response, response.Futures);
    #endregion GetFuturesResponse
    
    #region GetFutureOddsResponse
    def test_GetFutureOddsResponse_FutureOdds_ShouldReturnSuccess(self):
        response = Response.GetFutureOddsResponse(self.FutureOddsResponseText);
        self.assertIsInstance(response, Response.GetFutureOddsResponse);
        self.assertIsNotNone(response, response.FutureOdds);
        self.assertIsInstance(response.FutureOdds[0].future, Models.Future);    
    #endregion GetFutureOddsResponse

    #region GetScoresResponse
    def test_GetScoresRequest_Scores_ShouldReturnSuccess(self):
        response = Response.GetScoresResponse(self.ScoresResponseText);
        self.assertIsInstance(response, Response.GetScoresResponse);
        self.assertIsNotNone(response, response.Scores);
        self.assertIsInstance(response.Scores[0].game, Models.Game);
        self.assertIsInstance(response.Scores[0].period_scores[0], Models.PeriodScore);
    #endregion GetScoresResponse

if __name__=='__main__':
    unittest.main();