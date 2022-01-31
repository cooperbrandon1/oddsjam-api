#region Imports
from dataclasses import fields;
from datetime import date
from Base.ValidParameters import ValidSports, ValidSportsBooks;
from Base.CustomExceptions import SportError, SportsBookError;
#endregion Imports

def EnforceTypes(cls):
    field_types = {field.name: field.type for field in fields(cls)}
    for f in field_types:
        classAttr = getattr(cls,f);
        if(classAttr != None):
            if(f == 'sport' and classAttr not in ValidSports):
                raise SportError();
            elif((f == 'sportsbook' and classAttr not in ValidSportsBooks) or (f =='sports_book_name' and classAttr not in ValidSportsBooks)):
                raise SportsBookError();
            elif(isinstance(classAttr,field_types[f]) == False):
                raise TypeError(f + ' must be of type ' + field_types[f].__name__);
            elif('Date' in f):
                try:
                    date.fromisoformat(classAttr);
                except:
                    raise ValueError(f + ' must be in ISO-8601 format (ex. 11-01-2021)');
    return cls;