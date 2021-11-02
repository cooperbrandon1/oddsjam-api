class League():
    def __init__(cls,name: str = None):
        cls._name = name;

    @property
    def Name(cls):
        return cls._name;

    @Name.setter
    def Name(cls, newName):
        cls._name = newName;