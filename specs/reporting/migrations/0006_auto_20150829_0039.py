# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0005_auto_20150828_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='provider',
        ),
        migrations.AddField(
            model_name='site',
            name='provider',
            field=models.ForeignKey(blank=True, to='reporting.ColoProvider', null=True),
        ),
    ]
