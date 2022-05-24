from django.db import models
from django.conf import settings

from .enums import *


class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(blank=True, default=0)
    description = models.TextField(blank=True, default='', max_length=10000)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(blank=True, default=0)
    genre = models.CharField(blank=True, default='', max_length=1000)


class Journal (BookJournalBase):
    type = enum.EnumField(JournalType, default=JournalType.Bullet, blank=True)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='journals', on_delete=models.CASCADE)

