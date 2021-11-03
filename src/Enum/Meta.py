import enum

class StringEnumMeta(enum.EnumMeta):
    def __contains__(cls,item):
        for member in cls:
            if member.name.lower() == item.lower():
                return True;
            elif member.value.lower() == item.lower():
                return True;
        return False;

    def __getValueForString__(cls,item):
        for member in cls:
            if member.name.lower() == item.lower():
                return cls(member.value);
            elif member.value.lower() == item.lower():
                return cls(member.value)
        return False;