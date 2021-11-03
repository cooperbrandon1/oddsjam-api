from enum import Enum;
from Enum.Meta import StringEnumMeta;
class SportsEnum(Enum, metaclass=StringEnumMeta):
    football = 'football'
    basketball = 'basketball'
    baseball = 'baseball'
    mma = 'mma'
    boxing = 'boxing'
    hockey = 'hockey'
    soccer = 'soccer'
    tennis = 'tennis'
    golf = 'golf'
    motorsports = 'motorsports'
    esports = 'esports'