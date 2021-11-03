#region Imports
from dataclasses import fields;
from datetime import date
from Enum.Meta import StringEnumMeta;
#endregion Imports

def EnforceTypes(cls):
    field_types = {field.name: field.type for field in fields(cls)}
    for f in field_types:
        classAttr = getattr(cls,f);
        if(classAttr != None):
            StringToEnum = type(field_types[f]) == StringEnumMeta and isinstance(classAttr, str);
            #If the type of the destination attribute is an enum, and the incoming value is a string
            if(StringToEnum):
                #Check enums, ensuring that the incoming value is a valid value in the given enum
                if(field_types[f].__contains__(classAttr) == False):
                    raise ValueError(f + ' must be a valid value in ' + field_types[f].__name__);
                else:
                    setattr(cls,f,field_types[f].__getValueForString__(classAttr));
            elif(isinstance(classAttr,field_types[f]) == False):
                raise TypeError(f + ' must be of type ' + field_types[f].__name__);
            elif('Date' in f):
                try:
                    date.fromisoformat(classAttr);
                except:
                    raise ValueError(f + ' must be in ISO-8601 format (ex. 11-01-2021)');
    return cls;