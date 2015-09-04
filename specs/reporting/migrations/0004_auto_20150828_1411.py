# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0003_auto_20150827_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractweights',
            options={'ordering': ['date'], 'verbose_name': 'ContractWeights: Contract Scaling Weight'},
        ),
        migrations.AlterModelOptions(
            name='engineeringweights',
            options={'verbose_name': 'EngineeringWeights: Engineering Scaling Weight'},
        ),
        migrations.AlterModelOptions(
            name='priceweights',
            options={'verbose_name': 'PriceWeights: Price Scaling Weight'},
        ),
        migrations.AlterModelOptions(
            name='scaleweights',
            options={'verbose_name': 'ScaleWeights: Scalability Scaling Weight'},
        ),
        migrations.AlterModelOptions(
            name='securityweights',
            options={'verbose_name': 'SecurityWeights: Security Scaling Weight'},
        ),
        migrations.AlterModelOptions(
            name='siteaddress',
            options={'ordering': ['street'], 'verbose_name': 'Site Address'},
        ),
        migrations.AlterModelOptions(
            name='specsweights',
            options={'verbose_name': 'SpecsWeights: Overall Scaling Weight'},
        ),
        migrations.RemoveField(
            model_name='specs',
            name='region',
        ),
        migrations.AddField(
            model_name='scale',
            name='rack_positions_deployed',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='site',
            name='region',
            field=models.ForeignKey(blank=True, to='reporting.Region', null=True),
        ),
        migrations.AddField(
            model_name='siteaddress',
            name='postal_code',
            field=models.CharField(max_length=26, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=4, choices=[('CF', 'Cloudfront'), ('TX', 'Transit'), ('DX', 'Direct Connect'), ('EC2', 'EC2 Compute'), ('HPC', 'High Performance Computing'), ('VPC', 'Virtual Private Cloud'), ('AWS', 'AWS Production'), ('CORP', 'Corporate IT Production'), ('GPS', 'Global Payment Service'), ('S3', 'S3 Storage'), ('CMT', 'CMT'), ('CNN', 'Critical Network Node')]),
        ),
    ]
