# <code>oddsjam-api</code>: A lightweight OddsJam API wrapper

## V2 Update
V2 support is now available for the new endpoints/models listed at the [OddsJam Developer Page](https://developer.oddsjam.com/).  The client exposed by this package is backwards compatible, and runs in v1 by default. Versions can be switched as follows:
``` python
    from OddsJamClient import OddsJamClient;
    Client = OddsJamClient(YOUR_API_KEY);
    v1Results = Client.GetLeagues(); #Default v1 endpoints

    Client.UseV2();
    v2Results = Client.GetLeagues(); #v2 endpoints
```

This update comes with the following changes:
<ul>
<li>Type hinting for function calls is no longer available. Function calls will appear with <code>(*args: Any, **kwargs:Any) -> Any</code>. Please refer to the developer documentation for valid arguments.</li>
<li>The V2 client does <strong>not</strong> contain a GetMarkets() function.</li>
<li>The V2 client requires <i>at least one</i> argument for the GetOdds() function. This is due to the amount of data returned from the new V2 endpoint. Attempting a call to GetOdds() <i>without</i> a parameter will result in an <code>InvalidGetOddsV2Error</code>, and the endpoint will <i>not</i> be hit.</li>
</ul>
<br/>

## What is <code>oddsjam-api</code>?
<code>oddsjam-api</code> is a fast, lightweight wrapper for the [OddsJam API](https://developer.oddsjam.com/). It strives to be as intuitive to use as possible, providing strongly typed requests and responses to ensure predictability and consistency.



## How do I use it?
Start by installing the <code>oddsjam-api</code> package (currently only on TestPyPI):
``` 
    pip install oddsjam-api
```

Create an instance of the <code>OddsJamClient</code>:

``` python
    from OddsJamClient import OddsJamClient;
    Client = OddsJamClient(YOUR_API_KEY);
```

Then simply call whichever function you'd like to:

``` python 
    from OddsJamClient import OddsJamClient;
    Client = OddsJamClient(YOUR_API_KEY);
    GamesResponse = Client.GetGames();
```

Parameters are not required for any function call, but can be provided as desired:

``` python
    from OddsJamClient import OddsJamClient;
    Client = OddsJamClient(YOUR_API_KEY);
    GamesResponse = Client.GetGames(league='ncaa', sport='football');
```

Parameters will raise specific errors:

``` python
    GamesResponse = Client.GetGames(sport='curling'); 
    #Raises SportError, with a list of valid values

    OddsResponse = Client.GetOdds(sportsbook='212 Bet');
    #Raises SportsBookError, with a list of valid values
```

Note: Sport and SportsBook parameters are *case insensitive*

Accessing the object of a response requires accessing the response's object:

``` python    
    from OddsJamClient import OddsJamClient;
    Client = OddsJamClient(YOUR_API_KEY);
    GamesResponse = Client.GetGames();
    Games = GamesResponse.Games;
```

List comprehension can also be used to access objects:

``` python
    AwayTeams = [g.away_team for g in GamesResponse.Games];
```

Nested objects can be accessed similarly:

``` python
    OddsResponse = Client.GetOdds();
    print(OddsResponse.Odds[0].game.sport)
```

The raw response from the API is also accessible via the *RawResponse* property of any *Response* object:

``` python
    Raw = GamesResponse.RawResponse;
    Jobj = json.loads(raw);
```

## Built-in functions
Convert entire Odds collection to decimal, then back to American:
``` python
    OddsResponse = Client.GetOdds();
    OddsResponse.AsDecimal();
    OddsResponse.AsAmerican();
```

Convert individual Odds object to decimal, then back to American:
``` python
    OddsResponse = Client.GetOdds();
    FirstOdd = OddsResponse.Odds[0];
    FirstOdd.AsDecimal();
    FirstOdd.AsAmerican();
```

## Example usage
Flatten and output data using pandas:
``` python
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