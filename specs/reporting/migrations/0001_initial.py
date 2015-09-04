# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['code'],
                'verbose_name': 'Availability Zone',
            },
        ),
        migrations.CreateModel(
            name='ColoProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=90, blank=True)),
                ('portal_url', models.URLField(max_length=2048, blank=True)),
                ('gibd_owner', models.CharField(max_length=64, blank=True)),
                ('pmt_owner', models.CharField(max_length=64, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Colocation Provider',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=90, blank=True)),
                ('middle_name', models.CharField(max_length=90, blank=True)),
                ('last_name', models.CharField(max_length=90, blank=True)),
                ('title', models.CharField(max_length=90, blank=True)),
                ('email_address', models.EmailField(max_length=254, blank=True)),
                ('office_phone', models.CharField(max_length=45, blank=True)),
                ('mobile_phone', models.CharField(max_length=45, blank=True)),
                ('street', models.CharField(max_length=90, blank=True)),
                ('city', models.CharField(max_length=45, blank=True)),
                ('state', models.CharField(max_length=45, blank=True)),
                ('country', models.CharField(max_length=45, blank=True)),
                ('amazon_id', models.CharField(max_length=90, blank=True)),
                ('notes', models.TextField()),
                ('alternate', models.ForeignKey(blank=True, to='reporting.Contact', null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'verbose_name': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('negotioations', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('reporting', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('compliance', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('sla_violations', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContractWeights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('negotioations', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('reporting', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('compliance', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('sla_violations', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Contract Scaling Weights',
            },
        ),
        migrations.CreateModel(
            name='Engineering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colo_audit_score', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('non_impacting_events', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('impacting_events', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('dc_tiering_level', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EngineeringWeights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('colo_audit_score', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('non_impacting_events', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('impacting_events', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('dc_tiering_level', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
            ],
            options={
                'verbose_name': 'Engineering Scaling Weights',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_terms', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('invoice_performance', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('average_first_to_last_quote_delta', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('pue', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('per_unit_cost', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceWeights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('payment_terms', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('invoice_performance', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('average_first_to_last_quote_delta', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('pue', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('per_unit_cost', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
            ],
            options={
                'verbose_name': 'Price Scaling Weights',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=2, choices=[('NA', 'North America'), ('SA', 'South America'), ('EM', 'Europe, the Middle East and Africa'), ('AP', 'Asia Pacific')])),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['code'],
                'verbose_name': 'Region',
            },
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_management', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('contact_list', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('communications', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('staffing_model_level', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('mop', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('eop', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('black_gray_day_compliance', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('helpdesk_noc', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('helpdesk_noc_issue_request_resolution_time', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('maintenance_notifications', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('event_incident_notifications', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('post_event_incident_reporting', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('bms', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('number_of_sites_not_used_by_aws', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('rack_positions_available', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
                ('portal', models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScaleWeights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('account_management', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('contact_list', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('communications', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('staffing_model_level', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('mop', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('eop', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('black_gray_day_compliance', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('helpdesk_noc', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('helpdesk_noc_issue_request_resolution_time', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('maintenance_notifications', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('event_incident_notifications', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('post_event_incident_reporting', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('bms', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('number_of_sites_not_used_by_aws', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('rack_positions_available', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('portal', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
            ],
            options={
                'verbose_name': 'Scalability Scaling Weights',
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_list', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('average_response_time', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('issues', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('sla_violations', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('staffing_model_level', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityWeights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('contact_list', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('average_response_time', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('issues', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('sla_violations', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('staffing_model_level', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
            ],
            options={
                'verbose_name': 'Security Scaling Weights',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=3, choices=[('POP', 'POP'), ('CF', 'Cloudfront'), ('TX', 'Transit'), ('DX', 'Direct Connect'), ('EC2', 'EC2 Compute'), ('HPC', 'High Performance Computing'), ('VPC', 'Virtual Private Cloud'), ('AWS', 'AWS Production'), ('CORP', 'Corporate IT Production'), ('GPS', 'Global Payment Service'), ('S3', 'S3 Storage'), ('CMT', 'CMT')])),
                ('description', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['description'],
                'verbose_name': 'Service',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=7)),
                ('agile_no', models.CharField(max_length=10, blank=True)),
                ('project_name', models.CharField(max_length=64, blank=True)),
                ('tier_level', models.IntegerField(default=0, blank=True)),
                ('status', models.CharField(max_length=3, choices=[('PRD', 'In Production'), ('DEV', 'In Development')])),
                ('availability_zone', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='reporting.AvailabilityZone', null=True)),
                ('colo_audit_owner', models.ForeignKey(related_name='colo_audit_owner', blank=True, to='reporting.Contact', null=True)),
                ('dceo_owner', models.ForeignKey(related_name='dceo_owner', blank=True, to='reporting.Contact', null=True)),
                ('dco_owner', models.ForeignKey(related_name='dco_owner', blank=True, to='reporting.Contact', null=True)),
                ('event_contact', models.ForeignKey(related_name='event_contact', blank=True, to='reporting.Contact', null=True)),
            ],
            options={
                'ordering': ['code'],
                'verbose_name': 'Site',
            },
        ),
        migrations.CreateModel(
            name='SiteAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=90, null=True, blank=True)),
                ('city', models.CharField(max_length=45, null=True, blank=True)),
                ('state', models.CharField(max_length=45, null=True, blank=True)),
                ('country', models.CharField(max_length=45, null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
            ],
            options={
                'ordering': ['street'],
                'verbose_name': 'Site',
            },
        ),
        migrations.CreateModel(
            name='Specs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published_date', models.DateField(blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('contract', models.ForeignKey(blank=True, to='reporting.Contract', null=True)),
                ('engineering', models.ForeignKey(blank=True, to='reporting.Engineering', null=True)),
                ('price', models.ForeignKey(blank=True, to='reporting.Price', null=True)),
                ('region', models.ForeignKey(blank=True, to='reporting.Region', null=True)),
                ('scale', models.ForeignKey(blank=True, to='reporting.Scale', null=True)),
                ('security', models.ForeignKey(blank=True, to='reporting.Security', null=True)),
                ('site_code', models.ForeignKey(to='reporting.Site')),
            ],
            options={
                'ordering': ['site_code', 'published_date'],
                'verbose_name': 'SPECS Record',
            },
        ),
        migrations.CreateModel(
            name='SpecsWeights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('score_a', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('score_b', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('score_c', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('score_d', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('score_f', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('overall_weight_security', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('overall_weight_pricing', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('overall_weight_engineering', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('overall_weight_contract', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
                ('overall_weight_scalability', models.DecimalField(default=0, max_digits=5, decimal_places=3, blank=True)),
            ],
            options={
                'verbose_name': 'Overall Scaling Weights',
            },
        ),
        migrations.AddField(
            model_name='site',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='reporting.SiteAddress', null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='maintenance_contact',
            field=models.ForeignKey(related_name='maintenance_contact', blank=True, to='reporting.Contact', null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='payment_support_owner',
            field=models.ForeignKey(related_name='payment_support_owner', blank=True, to='reporting.Contact', null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='provider',
            field=models.ManyToManyField(to='reporting.ColoProvider', blank=True),
        ),
        migrations.AddField(
            model_name='site',
            name='security_owner',
            field=models.ForeignKey(related_name='security_owner', blank=True, to='reporting.Contact', null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_assessment_owner',
            field=models.ForeignKey(related_name='site_assessment_owner', blank=True, to='reporting.Contact', null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_ops_contact',
            field=models.ForeignKey(related_name='site_ops_contact', blank=True, to='reporting.Contact', null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_security_contact',
            field=models.ForeignKey(related_name='site_security_contact', blank=True, to='reporting.Contact', null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='sites',
            field=models.ManyToManyField(to='reporting.Site'),
        ),
        migrations.AddField(
            model_name='coloprovider',
            name='primary_account_contact',
            field=models.ForeignKey(related_name='primary_account_contact', blank=True, to='reporting.Contact'),
        ),
        migrations.AddField(
            model_name='coloprovider',
            name='primary_operations_contact',
            field=models.ForeignKey(related_name='primary_operations_contact', blank=True, to='reporting.Contact'),
        ),
        migrations.AddField(
            model_name='coloprovider',
            name='primary_sales_contact',
            field=models.ForeignKey(related_name='primary_sales_contact', blank=True, to='reporting.Contact'),
        ),
        migrations.AddField(
            model_name='coloprovider',
            name='primary_security_contact',
            field=models.ForeignKey(related_name='primary_security_contact', blank=True, to='reporting.Contact'),
        ),
    ]
