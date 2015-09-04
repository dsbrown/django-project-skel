# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0006_auto_20150829_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='provider',
        ),
        migrations.AddField(
            model_name='coloprovider',
            name='site',
            field=models.ManyToManyField(to='reporting.Site'),
        ),
    ]
