from django_enumfield import enum


class UserRole (enum.Enum):
    Guest = 0,
    SuperAdmin = 1
