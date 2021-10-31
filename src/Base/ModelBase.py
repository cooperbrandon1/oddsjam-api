class ModelBase():    
    @classmethod
    def fromDict(cls, dict: dict):
        objProps = dict.keys();
        instance = cls();
        for k in objProps:
            setattr(instance, str.capitalize(k.lower()), dict[k])
        return instance