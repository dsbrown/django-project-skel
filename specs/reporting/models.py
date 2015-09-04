###################################################################################
#                                   Django Reporting App
#                                          models.py
# Author: David S. Brown
# v1.0  CS      11 Aug 2015    Original
# v1.1  DSB     18 Aug 2015    Flushed out tables
# v1.2  CS      21 Aug 2015    Flushed out blank and null issues 
# v1.3  DSB     26 Aug 2015    Fixed numerous errors and problems that prevented it from being usable.
# v1.4  DSB     27 Aug 2015    Moved region key to Site, was in Spec, changed provider from many to many to Foreign key
#
####################################################################################

from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Specs(models.Model):
    published_date = models.DateField(blank=True)
    site_code = models.ForeignKey('Site')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    security = models.ForeignKey('Security', blank=True, null=True)
    price = models.ForeignKey('Price', blank=True, null=True)
    engineering = models.ForeignKey('Engineering', blank=True, null=True)
    contract = models.ForeignKey('Contract', blank=True, null=True) 
    scale = models.ForeignKey('Scale', blank=True, null=True) 
    #removed region
    def get_score_security(self):
       return self.security.get_score()
    def get_score_price(self):
       return self.price.get_score()
    def get_score_engineering(self):
       return self.engineering.get_score()
    def get_score_contract(self):
       return self.contract.get_score()
    def get_score_scale(self):
       return self.scale.get_score()
    def get_score(self):
       return (get_score_security*SpecsWeights.overallWeightSecurity + \
        get_score_price*SpecsWeights.overallWeightPricing + get_score_engineering*SpecsWeights.overallWeightEngineering + \
        get_score_contract*SpecsWeights.overallWeightContract + get_score_scale*SpecsWeights.overallWeightScalability )

    class Meta:
        ordering = ['site_code','published_date']
        verbose_name = 'SPECS Record'

    def __unicode__(self):
        return u'%s on %s' % (self.site_code.code, self.published_date)

class SpecsWeights(models.Model):
    date = models.DateField(blank=True)
    score_a = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    score_b = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    score_c = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    score_d = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    score_f = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    overall_weight_security = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    overall_weight_pricing = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    overall_weight_engineering = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    overall_weight_contract = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    overall_weight_scalability = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
  
    def get_grade_color(self, score):
        color = ''
        if score > SpecsWeights.ScoreB:
            color = 'green'
        elif score > SpecsWeights.ScoreC:
            color = 'lime'
        elif score > SpecsWeights.ScoreD:
            color = 'yellow'
        elif score > SpecsWeights.ScoreF:
            color = 'orange'
        else:
            color = 'red'
        return color

    class Meta:
        verbose_name = 'SpecsWeights: Overall Scaling Weight'
    def __unicode__(self):
        return u'%s' % (self.date)

class Security(models.Model):
    contact_list = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    average_response_time  = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    issues = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    sla_violations = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    staffing_model_level = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)

    def get_score_contact_list(self):
        return self.contact_list * SecurityWeights.contactsList
    def get_score_average_response_time(self):
        return self.average_response_time * SecurityWeights.average_response_time
    def get_score_issues(self):
        return self.issues * SecurityWeights.issues
    def get_score_sla_violations(self):
        return self.sla_violations * SecurityWeights.sla_violations
    def get_score_staffing_model_level(self):
        return self.staffing_model_level * SecurityWeights.staffing_model_level
    def get_score(self):
        return (self.get_score_contact_list + self.get_score_average_response_time + self.get_score_issues + \
        self.get_score_sla_violations + self.get_score_staffing_model_level)
    class Meta:
        verbose_name = 'Security Scores'

    def __unicode__(self):
        #return u'%s' % (self.verbose_name)
        return u'%s' % (self.pk)

class SecurityWeights(models.Model):
    date = models.DateField(blank=True)
    contact_list = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    average_response_time = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    issues = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    sla_violations = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    staffing_model_level = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)

    class Meta:
        verbose_name = 'SecurityWeights: Security Scaling Weight'
    def __unicode__(self):
        return u'%s' % (self.date)

class Price(models.Model):
    payment_terms = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    invoice_performance = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    average_first_to_last_quote_delta = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    pue = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    per_unit_cost = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    def get_score_payment_terms(self):
        return self.payment_terms * PriceWeights.payment_terms
    def get_score_invoice_performance(self):
        return self.invoice_performance * PriceWeights.invoice_performance
    def get_score_average_first_to_last_quote_delta(self):
        return self.average_first_to_last_quote_delta * PriceWeights.average_first_to_last_quote_delta
    def get_score_pue(self):
        return self.pue * PriceWeights.pue
    def get_score_per_unit_cost(self):
        return self.per_unit_cost * PriceWeights.per_unit_cost
    def get_score(self):
        return (self.get_score_payment_terms + self.get_score_invoice_performance + self.get_score_average_first_to_last_quote_delta + \
        self.get_score_pue + self.get_score_per_unit_cost)
    class Meta:
        verbose_name = 'Price Scores'
    def __unicode__(self):
        return u'%s' % (self.pk)

class PriceWeights(models.Model):
    date = models.DateField(blank=True)
    payment_terms = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    invoice_performance = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    average_first_to_last_quote_delta = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    pue = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    per_unit_cost = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)

    class Meta:
        verbose_name = 'PriceWeights: Price Scaling Weight'
    def __unicode__(self):
        return u'%s' % (self.date)
    
class Engineering(models.Model):
    colo_audit_score = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    non_impacting_events = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    impacting_events = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    dc_tiering_level = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)

    def get_score_colo_audit_score(self):
        return self.colo_audit_score * EngineeringWeights.colo_audit_score
    def get_score_non_impacting_events(self):
        return self.non_impacting_events * EngineeringWeights.non_impacting_events
    def get_score_impacting_events(self):
        return self.impacting_events * EngineeringWeights.impacting_events
    def get_score_dc_tiering_level(self):
        return self.dc_tiering_level * EngineeringWeights.dc_tiering_level
    def get_score(self):
        return (self.get_score_colo_audit_score + self.get_score_non_impacting_events + \
            self.get_score_impacting_events + self.get_score_dc_tiering_level)

    class Meta:
        verbose_name = 'Engineering Scores'
    def __unicode__(self):
        return u'%s' % (self.pk)


class EngineeringWeights(models.Model):
    date = models.DateField(blank=True)
    colo_audit_score = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    non_impacting_events = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    impacting_events = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    dc_tiering_level = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)

    class Meta:
        verbose_name = 'EngineeringWeights: Engineering Scaling Weight'
    def __unicode__(self):
        return u'%s' % (self.date)

class Contract(models.Model):
    negotiations = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    reporting = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    compliance = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    sla_violations = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)

    def get_score_negotiations(self):
        return self.negotiations * ContractWeights.negotiations
    def get_score_reporting(self):
        return self.reporting * ContractWeights.reporting
    def get_score_compliance(self):
        return self.compliance * ContractWeights.compliance
    def get_score_sla_violations(self):
        return self.sla_violations * ContractWeights.sla_violations
    def get_score(self):
        return ( self.get_score_negotiations + self.get_score_reporting + self.get_score_compliance + self.get_score_sla_violations)
   
    class Meta:
        verbose_name = 'Contract Scores'
    def __unicode__(self):
        return u'%s' % (self.pk)

class ContractWeights(models.Model):
    date = models.DateField(blank=True)
    negotiations = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    reporting = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    compliance = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    sla_violations = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'ContractWeights: Contract Scaling Weight'

    def __unicode__(self):
        return u'%s' % (self.date)

class Scale(models.Model):
    account_management = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    contact_list = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    communications = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    staffing_model_level = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    mop = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    eop = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    black_gray_day_compliance = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    helpdesk_noc = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    helpdesk_noc_issue_request_resolution_time = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    maintenance_notifications = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    event_incident_notifications = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    post_event_incident_reporting = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    bms = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    number_of_sites_not_used_by_aws = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    rack_positions_available = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    rack_positions_deployed = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    portal = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)

    def get_score_account_management(self):
        return self.account_management * ScaleWeights.account_management
    def get_score_contact_list(self):
        return self.contact_list * ScaleWeights.contact_list
    def get_score_communications(self):
        return self.communications * ScaleWeights.communications
    def get_score_staffing_model_level(self):
        return self.staffing_model_level * ScaleWeights.staffing_model_level
    def get_score_mop(self):
        return self.mop * ScaleWeights.mop
    def get_score_eop(self):
        return self.eop * ScaleWeights.eop
    def get_score_black_gray_day_compliance(self):
        return self.black_gray_day_compliance * ScaleWeights.black_gray_day_compliance
    def get_score_helpdesk_noc(self):
        return self.helpdesk_noc * ScaleWeights.helpdesk_noc
    def get_score_helpdesk_noc_issue_request_resolution_time(self):
        return self.helpdesk_noc_issue_request_resolution_time * ScaleWeights.helpdesk_noc_issue_request_resolution_time
    def get_score_maintenance_notifications(self):
        return self.maintenance_notifications * ScaleWeights.maintenance_notifications
    def get_score_event_incident_notifications(self):
        return self.event_incident_notifications * ScaleWeights.event_incident_notifications
    def get_score_post_event_incident_reporting(self):
        return self.post_event_incident_reporting * ScaleWeights.post_event_incident_reporting
    def get_score_bms(self):
        return self.bms * ScaleWeights.bms
    def get_score_number_of_sites_not_used_by_aws(self):
        return self.number_of_sites_not_used_by_aws * ScaleWeights.number_of_sites_not_used_by_aws
    def get_score_rack_positions_available(self):
        return self.rack_positions_available * ScaleWeights.rack_positions_available
    def get_score_portal(self):
        return self.portal * ScaleWeights.portal

    def get_score(self):
        return (get_score_account_management + get_score_contact_list + get_score_communications + \
                get_score_staffing_model_level + get_score_mop + get_score_eop + \
                get_score_black_gray_day_compliance + get_score_helpdesk_noc + \
                get_score_helpdesk_noc_issue_request_resolution_time + get_score_maintenance_notifications + \
                get_score_event_incident_notifications + get_score_post_event_incident_reporting + \
                get_score_bms + get_score_number_of_sites_not_used_by_aws + \
                get_score_rack_positions_available + get_score_portal )

    class Meta:
        verbose_name = 'Scalability Scores'
    def __unicode__(self):
        return u'%s' % (self.pk)

class ScaleWeights(models.Model):
    date = models.DateField(blank=True)
    account_management = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    contact_list = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    communications = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    staffing_model_level = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    mop = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    eop = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    black_gray_day_compliance = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    helpdesk_noc = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    helpdesk_noc_issue_request_resolution_time = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    maintenance_notifications = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    event_incident_notifications = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    post_event_incident_reporting = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    bms = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    number_of_sites_not_used_by_aws = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    rack_positions_available = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)
    portal = models.DecimalField(max_digits=5, decimal_places=3, default=0, blank=True)

    class Meta:
        verbose_name = 'ScaleWeights: Scalability Scaling Weight'
    def __unicode__(self):
        return u'%s' % (self.date)

class Region(models.Model):
    NORTHAMERICA = 'NA'
    SOUTHAMERICA = 'SA'
    EMEA = 'EM'
    ASIA = 'AP'
    REGION = (
        ('NA', 'North America'),
        ('SA', 'South America'),
        ('EM', 'Europe, the Middle East and Africa'),
        ('AP', 'Asia Pacific'),
    )
    code = models.CharField(max_length=2, choices=REGION)
    description = models.CharField(max_length=128)
    def __unicode__(self):
        return u'%s (%s)' % (self.description, self.code)
  
    def region_name(self,region_code):
        REGION_NAME = {
            'NA' : 'North America',
            'SA' : 'South America',
            'EM' : 'Europe, the Middle East and Africa',
            'AP' : 'Asia Pacific',
        }
        return REGION_NAME[region_code]

    class Meta:
        ordering = ['code']
        verbose_name = 'Region Name'

class AvailabilityZone(models.Model):
    code = models.CharField(max_length=45) 
    description = models.TextField()
    def get_code(self, site_code):
        return site_code[:3]
    def __unicode__(self):
        return u'%s' % (self.code)
    class Meta:
        ordering = ['code']
        verbose_name = 'Availability Zone'

class SiteAddress(models.Model):
    street = models.CharField(max_length=90, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    postal_code = models.CharField(max_length=26, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.street)
    class Meta:
        ordering = ['street']
        verbose_name = 'Site Address'

class Contact(models.Model):
    first_name = models.CharField(max_length=90, blank=True)
    middle_name = models.CharField(max_length=90, blank=True)
    last_name = models.CharField(max_length=90, blank=True)
    title = models.CharField(max_length=90, blank=True)
    email_address = models.EmailField(blank=True)
    office_phone = models.CharField(max_length=45, blank=True)
    mobile_phone = models.CharField(max_length=45, blank=True)
    street = models.CharField(max_length=90, blank=True)
    city = models.CharField(max_length=45, blank=True)
    state = models.CharField(max_length=45, blank=True)
    country = models.CharField(max_length=45, blank=True)
    amazon_id = models.CharField(max_length=90, blank=True)
    alternate = models.ForeignKey('Contact', blank=True, null=True)
    notes = models.TextField()
    def __unicode__(self):
        return u'%s' % (self.name)
    class Meta:
        ordering = ['last_name','first_name']
        verbose_name = 'Contact'


class Site(models.Model):
    STATUS_TYPE = (
        ('PRD', 'In Production'),
        ('DEV', 'In Development'),
    )
    code = models.CharField(max_length=7)
    agile_no = models.CharField(max_length=10, blank=True)
    project_name = models.CharField(max_length=64, blank=True)
    availability_zone = models.ForeignKey('AvailabilityZone', blank=True, null=True, on_delete=models.SET_NULL)
    region = models.ForeignKey('Region', blank=True, null=True) 
    tier_level = models.IntegerField(default=0, blank=True)
    location = models.ForeignKey('SiteAddress', blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=3, choices=STATUS_TYPE)
    site_ops_contact = models.ForeignKey('Contact', blank=True, null=True, related_name="site_ops_contact")
    site_security_contact = models.ForeignKey('Contact', blank=True, null=True, related_name="site_security_contact")
    maintenance_contact = models.ForeignKey('Contact', blank=True, null=True, related_name="maintenance_contact")
    event_contact = models.ForeignKey('Contact', blank=True, null=True, related_name="event_contact")
    dceo_owner = models.ForeignKey('Contact', blank=True, null=True, related_name="dceo_owner")
    dco_owner = models.ForeignKey('Contact', blank=True, null=True, related_name="dco_owner")
    security_owner = models.ForeignKey('Contact', blank=True, null=True, related_name="security_owner")
    colo_audit_owner = models.ForeignKey('Contact', blank=True, null=True, related_name="colo_audit_owner")
    site_assessment_owner = models.ForeignKey('Contact', blank=True, null=True, related_name="site_assessment_owner")
    payment_support_owner =  models.ForeignKey('Contact', blank=True, null=True, related_name="payment_support_owner")

    def __unicode__(self):
        return u'%s' % (self.code)
    def get_all_specs(self):
        return Specs.object.filter(site=self)
    def get_latest_specs(self):
        specs = Specs.objects.filter(site=self).order_by('published')[0]
        return specs
    def has_specs(self):
        return (Specs.objects.filter(site=self).count() > 0)
    def get_specs_count(self):
        return Specs.objects.filter(site=self).count()
    def get_grade(self, element):
        color = ''
        if element == 'security':
            color = 'green'
        elif element == 'price':
            color = 'green'
        elif element == 'engineering':
            color = 'yellow'
        elif element == 'contract':
            color = 'red'
        elif element == 'scale':
            color = 'orange'
        return color
    def get_absolute_url(self):
        return reverse('reporting.views.site_by_code', args=[str(self.code)])
    def status_name(self,service_code):
        STATUS_NAME = {
            'PRD' : 'In Production',
            'DEV' : 'In Development',
        }
        return STATUS_NAME[service_code]
    class Meta:
        ordering = ['code']
        verbose_name = 'AWS Site Information'
        
class ColoProvider(models.Model):
    name = models.CharField(max_length=90, blank=True)
    primary_account_contact = models.ForeignKey('Contact', blank=True, null=True, related_name="primary_account_contact")
    primary_sales_contact = models.ForeignKey('Contact', blank=True, null=True, related_name="primary_sales_contact")
    primary_operations_contact = models.ForeignKey('Contact', blank=True, null=True, related_name="primary_operations_contact")
    primary_security_contact = models.ForeignKey('Contact', blank=True, null=True, related_name="primary_security_contact")
    portal_url = models.URLField(max_length=2048, blank=True, null=True)
    site = models.ManyToManyField(Site)
    # should be in site -> tier_level = models.IntegerField(default=0, blank=True)
    gibd_owner = models.CharField(max_length=64, blank=True, null=True)
    pmt_owner = models.CharField(max_length=64, blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.name)
    class Meta:
        ordering = ['name']
        verbose_name = 'Colocation Provider'

class Service(models.Model):
    CLOUDFRONT = "CF"
    TRANSIT = "TX"
    DIRECT_CONNECT = "DX"
    EC2_COMPUTE = "EC2"
    HIGH_PERFORMANCE_COMPUTING = "HPC"
    VIRTUAL_PRIVATECLOUD = "VPC"
    AWS_PRODUCTION = "AWS"
    CORP_IT = "CORP"
    GLOBAL_PAYMENT_SERVICE = "GPS"
    S3_STORAGE = "S3"
    CMT = "CMT"
    CNN = "CNN"
    SERVICE_TYPE = (
        (CLOUDFRONT, 'Cloudfront'),
        (TRANSIT, 'Transit'),
        (DIRECT_CONNECT, 'Direct Connect'),
        (EC2_COMPUTE, 'EC2 Compute'),
        (HIGH_PERFORMANCE_COMPUTING, 'High Performance Computing'),
        (VIRTUAL_PRIVATECLOUD, 'Virtual Private Cloud'),
        (AWS_PRODUCTION, 'AWS Production'),
        (CORP_IT, 'Corporate IT Production'),
        (GLOBAL_PAYMENT_SERVICE, 'Global Payment Service'),
        (S3_STORAGE, 'S3 Storage'),
        (CMT, 'CMT'),
        (CNN, 'Critical Network Node'),
    )
    name = models.CharField(max_length=4, choices=SERVICE_TYPE)
    description = models.CharField(max_length=45)
    sites = models.ManyToManyField(Site)

    def service_name(self,service_code):
        SERVICE_NAME = {
            'CF' : 'Cloudfront',
            'TX' : 'Transit',
            'DX' : 'Direct Connect',
            'EC2' : 'EC2 Compute',
            'HPC' : 'High Performance Computing',
            'VPC' : 'Virtual Private Cloud',
            'PROD' : 'AWS Production',
            'CORP' : 'Corporate IT Production',
            'GPS' : 'Global Payment Service',
            'S3' : 'S3 Storage',
            'CMT' : 'CMT',
            'CNN' : 'CNN',
        }
        return SERVICE_NAME[service_code]

    def __unicode__(self):
        return u'%s Service' % (self.name)       
    class Meta:
        ordering = ['description']
        verbose_name = 'Service'
"""
RECENT CHANGES
Migrations for 'reporting':
  0004_auto_20150828_1411.py:
    - Change Meta options on contractweights
    - Change Meta options on engineeringweights
    - Change Meta options on priceweights
    - Change Meta options on scaleweights
    - Change Meta options on securityweights
    - Change Meta options on siteaddress
    - Change Meta options on specsweights
    - Remove field region from specs
    - Add field rack_positions_deployed to scale
    - Add field region to site
    - Add field postal_code to siteaddress
    - Alter field name on service
"""
