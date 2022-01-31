#region Imports
from Base.EnforceTypes import EnforceTypes;
#endregion Imports

class ModelBase:    
    @classmethod
    def fromDict(cls, dict: dict):
        objProps = dict.keys();
        instance = cls();
        for k in objProps:
            try:
                setattr(instance, k, dict[k])
            except Exception as ex:
                return ex;
        return instance

    def __post_init__(cls):
        EnforceTypes(cls);