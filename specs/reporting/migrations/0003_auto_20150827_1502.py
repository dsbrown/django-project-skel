# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_auto_20150827_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Contract Scores'},
        ),
        migrations.AlterModelOptions(
            name='engineering',
            options={'verbose_name': 'Engineering Scores'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Price Scores'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['code'], 'verbose_name': 'Region Name'},
        ),
        migrations.AlterModelOptions(
            name='scale',
            options={'verbose_name': 'Scalability Scores'},
        ),
        migrations.AlterModelOptions(
            name='security',
            options={'verbose_name': 'Security Scores'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['code'], 'verbose_name': 'AWS Site Information'},
        ),
    ]
