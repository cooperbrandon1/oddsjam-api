#region Imports
import sys;
sys.path.append('././src');
sys.path.append('./');
from OddsJamClient import OddsJamClient;
import Response;
import unittest;
from unittest import mock;
import json;
import os
absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
parentDirectory = os.path.dirname(fileDirectory)
dataPath = os.path.join(parentDirectory, 'TestData/')   
#endregion Imports

#region Mock requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code, text):
            self.json_data = json_data
            self.status_code = status_code
            self.text = text

        def json(self):
            return self.json_data
        
        def text(self):
            return self.text;

    if '/games' in args[0]:
        return MockResponse(getJSON('GetGamesResponse'), 200, getText('GetGamesResponse'))
    elif '/leagues' in args[0]:
        return MockResponse(getJSON('GetLeaguesResponse'), 200, getText('GetLeaguesResponse'))
    elif '/markets' in args[0]:
        return MockResponse(getJSON('GetMarketsResponse'), 200, getText('GetMarketsResponse'))
    elif '/futures' in args[0]:
        return MockResponse(getJSON('GetFuturesResponse'), 200, getText('GetFuturesResponse'))
    elif '/future-odds' in args[0]:
        return MockResponse(getJSON('GetFutureOddsResponse'), 200, getText('GetFutureOddsResponse'))
    else:
        return MockResponse(getJSON('GetOddsResponse'), 200, getText('GetOddsResponse'))
 
    return MockResponse(None, 404)
#endregion Mock requests.get

def getJSON(fileName):
    with(open(dataPath+fileName+'.json') as f):
        return json.load(f);

def getText(fileName):
    with(open(dataPath+fileName+'.json') as f):
        j = json.load(f);
        return json.dumps(j);

class test_RequestIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.Client = OddsJamClient('MOCK_API_KEY');

    #region Success 
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_GetGames(self, mock_get):
        response = self.Client.GetGames();
        self.assertIsNot(None,response.Games);
        self.assertIsInstance(response,Response.GetGamesResponse);

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_GetLeagues(self, mock_get):
        response = self.Client.GetLeagues();
        self.assertIsNot(None,response.Leagues);
        self.assertIsInstance(response,Response.GetLeaguesResponse);

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_GetMarkets(self, mock_get):
        Client = OddsJamClient('MOCK_API_KEY');
        response = self.Client.GetMarkets();
        self.assertIsNot(None,response.Markets);
        self.assertIsInstance(response,Response.GetMarketsResponse);

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_GetOdds(self, mock_get):
        response = self.Client.GetOdds();
        self.assertIsNot(None,response.Odds);
        self.assertIsInstance(response,Response.GetOddsResponse);

        
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_GetFutures(self, mock_get):
        response = self.Client.GetFutures();
        self.assertIsNot(None,response.Futures);
        self.assertIsInstance(response,Response.GetFuturesResponse);
        
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_GetFutureOdds(self, mock_get):
        response = self.Client.GetFutureOdds();
        self.assertIsNot(None,response.FutureOdds);
        self.assertIsInstance(response,Response.GetFutureOddsResponse);
    #endregion Success

if __name__ == '__main__':
    pass;
    unittest.main();