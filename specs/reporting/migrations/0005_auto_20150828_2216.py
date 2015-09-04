# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_auto_20150828_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coloprovider',
            name='gibd_owner',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='coloprovider',
            name='pmt_owner',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='coloprovider',
            name='portal_url',
            field=models.URLField(max_length=2048, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='coloprovider',
            name='primary_account_contact',
            field=models.ForeignKey(related_name='primary_account_contact', blank=True, to='reporting.Contact', null=True),
        ),
        migrations.AlterField(
            model_name='coloprovider',
            name='primary_operations_contact',
            field=models.ForeignKey(related_name='primary_operations_contact', blank=True, to='reporting.Contact', null=True),
        ),
        migrations.AlterField(
            model_name='coloprovider',
            name='primary_sales_contact',
            field=models.ForeignKey(related_name='primary_sales_contact', blank=True, to='reporting.Contact', null=True),
        ),
        migrations.AlterField(
            model_name='coloprovider',
            name='primary_security_contact',
            field=models.ForeignKey(related_name='primary_security_contact', blank=True, to='reporting.Contact', null=True),
        ),
    ]
