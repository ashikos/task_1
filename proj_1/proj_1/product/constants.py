import enum


class ChoiceAdapter(enum.IntEnum):
    @classmethod
    def choices(cls):
        return ((item.value, item.name.replace("_", " ")) for item in cls)

    @classmethod
    def values(cls):
        return [item.value for item in cls]


