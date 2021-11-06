# <code>oddsjam-api</code>: A lightweight OddsJam API wrapper

## What is <code>oddsjam-api</code>?
<code>oddsjam-api</code> is a fast, lightweight wrapper for the [OddsJam API](https://developer.oddsjam.com/getting-started). It strives to be as intuitive to use as possible, providing strongly typed requests and responses to ensure predictability and consistency.

## How do I use it?
Start by installing the <code>oddsjam-api</code> package (currently only on TestPyPI):
```
    pip install -i https://test.pypi.org/simple/ oddsjam-api
```

Create an instance of the <code>OddsJamClient</code>:

```
    from OddsJamClient import OddsJamClient;
    Client = OddsJamClient(YOUR_API_KEY);
```

Then simply call whichever function you'd like to:

```    
    from OddsJamClient import OddsJamClient;
    Client = OddsJamClient(YOUR_API_KEY);
    GamesResponse = Client.GetGames();
```

Parameters are not required for any function call, but can be provided as desired:

```
    from OddsJamClient import OddsJamClient;
    from Enum.SportsEnum import SportsEnum;
    Client = OddsJamClient(YOUR_API_KEY);
    GamesResponse = Client.GetGames(league='ncaa', sport=SportsEnum.football);
```

And can be accessed by as parsed objects:

```
    AwayTeams = [g.away_team for g in GamesResponse.Games];
```

Nested objects can be accessed similarly:

```
    OddsResponse = Client.GetOdds();
    print(OddsResponse.Odds[0].game.sport)
```

The raw response from the API is also accessible via the *RawResponse* property of any *Response* object:

```
    Raw = GamesResponse.RawResponse;
    Jobj = json.loads(raw);
```