import Base;

class SportError(Exception):
    def __init__(self, *args: object) -> None:
        b = ', '.join(map(str,Base.ValidParameters.ValidSports));
        self.message = 'Sport parameter must be one of the following values (case insensitive): ' + b;
        super().__init__(self.message);

class SportsBookError(Exception):
    def __init__(self, *args: object) -> None:
        b = ', '.join(map(str,Base.ValidParameters.ValidSportsBooks));
        self.message = 'SportsBook parameter must be one of the following values (case insensitive): ' + b;
        super().__init__(self.message);