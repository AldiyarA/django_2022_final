from django_enumfield import enum


class JournalType (enum.Enum):
    Bullet = 0,
    Food = 1,
    Travel = 2,
    Sport = 3
