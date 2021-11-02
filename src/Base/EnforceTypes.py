#region Imports
from dataclasses import fields;
from datetime import date;
#endregion Imports

class EnforceTypes:
    def __init__(cls):
        field_types = {field.name: field.type for field in fields(cls)}
        for f in field_types:
            classAttr = getattr(cls,f);
            if(classAttr != None):
                if(isinstance(classAttr,field_types[f]) == False):
                    raise TypeError(f + ' must be of type ' + field_types[f].__name__);
                elif('Date' in f):
                    try:
                        date.fromisoformat(classAttr);
                    except:
                        raise ValueError(f + ' must be in ISO-8601 format (ex. 11-01-2021)');