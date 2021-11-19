# <code>oddsjam-api</code>: A lightweight OddsJam API wrapper

## What is <code>oddsjam-api</code>?
<code>oddsjam-api</code> is a fast, lightweight wrapper for the [OddsJam API](https://developer.oddsjam.com/getting-started). It strives to be as intuitive to use as possible, providing strongly typed requests and responses to ensure predictability and consistency.


## How do I use it?
Start by installing the <code>oddsjam-api</code> package (currently only on TestPyPI):
```
    pip install oddsjam-api
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
    Client = OddsJamClient(YOUR_API_KEY);
    GamesResponse = Client.GetGames(league='ncaa', sport='football');
```

Parameters will raise specific errors:

```
    GamesResponse = Client.GetGames(sport='curling'); 
    #Raises SportError, with a list of valid values

    OddsResponse = Client.GetOdds(sportsbook='212 Bet');
    #Raises SportsBookError, with a list of valid values
```

Note: Sport and SportsBook parameters are *case insensitive*

Accessing the object of a response requires accessing the response's object:

```    
    from OddsJamClient import OddsJamClient;
    Client = OddsJamClient(YOUR_API_KEY);
    GamesResponse = Client.GetGames();
    Games = GamesResponse.Games;
```

List comprehension can also be used to access objects:

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

## Built-in functions
Convert entire Odds collection to decimal, then back to American:
```
    OddsResponse = Client.GetOdds();
    OddsResponse.AsDecimal();
    OddsResponse.AsAmerican();
```

Convert individual Odds object to decimal, then back to American:
```
    OddsResponse = Client.GetOdds();
    FirstOdd = OddsResponse.Odds[0];
    FirstOdd.AsDecimal();
    FirstOdd.AsAmerican();
```

## Example usage
Flatten and output data using pandas:
```
    import pandas as pd;
    from OddsJamClient import OddsJamClient;

    Client = OddsJamClient(YOUR_API_KEY);
    Odds = Client.GetOdds().Odds;
    df = pd.DataFrame(Odds);

    #Lambda over rows to extract just the ID from the 'game' object in each row
    df['game'] = df.apply(lambda row: row['game']['id'], axis=1)
    
    #Get odds for Moneyline markets only
    df = df.loc[df['market_name'] == 'Moneyline']
```