#region Imports
import Enum;
#endregion Imports

class RequestBase():
    def __init__(cls):
        cls.ApiPath = None;
    
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
        elif(type(arg) is Enum.SportsEnum or type(arg) is Enum.SportsBooksEnum):
            return str(arg.value)