from OddsJamClient import OddsJamClient;
from Models import Game;
from Enum import SportsEnum;
import pandas as pd;
from pandas.io.json import json_normalize;
Client = OddsJamClient('e7803d61-d16a-4e1d-b3b8-406ece9b6483')
response = Client.GetLeagues();
print(pd.DataFrame(response.Leagues))
# print(response.flatten_json())