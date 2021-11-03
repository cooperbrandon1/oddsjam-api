from OddsJamClient import OddsJamClient;

b = OddsJamClient('e7803d61-d16a-4e1d-b3b8-406ece9b6483')
r = b.GetFutureOdds(page='1');
print(r.FutureOdds);