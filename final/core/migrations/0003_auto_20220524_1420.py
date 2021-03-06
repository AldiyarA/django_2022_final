# Generated by Django 2.2.27 on 2022-05-24 08:20

import core.enums
from django.db import migrations
import django_enumfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='type',
            field=django_enumfield.db.fields.EnumField(blank=True, default=0, enum=core.enums.JournalType),
        ),
    ]
