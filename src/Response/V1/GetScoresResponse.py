#region Imports
import json;
from Models.V1 import Score, Game, PeriodScore;
from Base import ResponseBase;
#endregion Imports

class GetScoresResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        self.Scores = self.ParseResponse(response);
        self.Type = 'American';
        
    def ParseResponse(self, response:str):
        try:
            obj = json.loads(response);
            scoresObject = [Score.fromDict(m) for m in obj];
            for o in scoresObject:
                o.game = Game.fromDict(o.game);
                parsedPeriodScores = [];
                for p in o.period_scores:
                    parsedPeriodScores.append(PeriodScore.fromDict(p));
                o.period_scores = parsedPeriodScores;
            return scoresObject;
        except Exception as ex:
            return ex;