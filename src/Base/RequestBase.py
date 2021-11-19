#region Imports
from Base.EnforceTypes import EnforceTypes;
from Base.ValidParameters import ValidSportsBooks, ValidSports;
from Base.CustomExceptions import SportError;
#endregion Imports

class RequestBase:

    @classmethod
    def GetArgString(cls):  
        #Get the list of attributes of the given subclass 
        props = [i for i in cls.__dict__.keys() if i[:1] != '_' and i != 'ApiPath'];
        #Get any populated attributes (e.g Sport = Sports.Football)
        #And convert them to a type that can be appended to a querystring
        #Not using urllib here 
        arguments = {p:cls.ConvertArg(getattr(cls,p)) for p in props if getattr(cls,p) != None}
        argStr = '&'
        argStr = ('&'.join("{!s}={!s}".format(key.lower(),val.lower().replace("'",'')) for (key,val) in arguments.items()))
        if(len(argStr) > 1):
            return argStr;
        return '';
    
    @classmethod
    def ConvertArg(cls,arg):
        if(type(arg) is int):
            return str(arg)

    def __post_init__(cls):
        EnforceTypes(cls);
