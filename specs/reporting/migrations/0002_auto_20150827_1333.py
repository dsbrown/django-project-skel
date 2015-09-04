# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='negotioations',
            new_name='negotiations',
        ),
        migrations.RenameField(
            model_name='contractweights',
            old_name='negotioations',
            new_name='negotiations',
        ),
    ]
