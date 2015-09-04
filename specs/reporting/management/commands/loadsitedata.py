###################################################################################
#                     Django Management Command loadsitedate
#
# Description:
#     Takes Excel spreadsheets with the site data
#     and writes it into the appropriate tables. The program is invoked as:
#
#     %python manage.py loadsitedata --path /Users/browdavi/Prog/SPECS/Datasource/Agile_data_by_SiteID_v1.4.xlsx
#
#     etc.
# v1.0  DSB     18 Aug 2015     Original program
# v1.1  DSB     26 Aug 2015     Modified, added extract by column name
# v1.2  DSB     31 Aug 2015     Finally fixed that pesky Coloprovider many to many relationship
#
####################################################################################

from django.core.management.base import BaseCommand, CommandError
from reporting.models import Site, Service, SiteAddress, ColoProvider, Region, AvailabilityZone
from os.path import isfile, join, splitext
from openpyxl import load_workbook
from django.apps import apps 
SUPPORTED_FORMATS = ('.xlsx', '.xlsm', '.xltx', '.xltm')

"""
    From the Agile Site spreadsheet used in Site
    code
    agile_no
    region
    availability_zone
    status
    provider

    From the Agile Site spreadsheet used in Service:
    service

    From the Agile Site spreadsheet used in SiteAddress:
    SiteAddress:
    street  
    city    
    state   
    country 
    postal_code
"""
class Command(BaseCommand):
    help = 'Loads the score site tables'

    def add_arguments(self, parser):
        parser.add_argument("--path", nargs="?", dest="path", required=True, 
                    help="Path to excel file")

    # Validates excel file can be processed 
    def valid_excel_file(self, xfile):
        if isfile(xfile) and not xfile.startswith('~'):
            (root,ext) = splitext(xfile)
            if ext.lower() in SUPPORTED_FORMATS:
                return xfile
            else:
                return ""

    def handle(self, *args, **options):
        path = options['path']
        #check if file is valid before continuing
        if self.valid_excel_file(path):
            self.stdout.write('Processing file - %s' % path)
            self.parse(path)
        else:
            raise CommandError('Path "%s" is not a valid excel file' % path)

    def get_rows(self,ws):
        headers=[0]
        first_row = True
        rows = []
        for row in ws.rows:
            c = 0
            t = {}
            for cell in row:
                if first_row:
                    headers[0]+=1
                    h=cell.value.lower()                               #All columns in the model are lower case!
                    h=h.strip()
                    headers.append(h)
                    self.stdout.write('Column Header [%s]'%h)
                else:
                     c += 1
                     t[headers[c]] = cell.value
            if first_row:
                first_row = False
                continue
            rows.append(t)
        return rows

    def parse(self, path):
        self.stdout.write('Parsing site file at %s'%path)
        wb = load_workbook(filename=path, data_only=True)
        ws = wb.worksheets[0]
        rows = self.get_rows(ws)
        for row in rows:
            self.process_row(row)

    def process_row(self, row):
        #check if we have a site code defined 
        # need to modify below for a dictionary now
        #
        print "Processing Row"
        if row['code']:
            # get or find the Site object  
            # I left agile_code out because its not uniquie and may cause problems
            site, created = Site.objects.get_or_create(code=row['code'],status=row['status'])
            self.stdout.write("site code = "+ row['code'])
            print "Created Site %s"%site
            
            #if zone is defined, get or create the record to set reference 
            #to Site object 
            if row['availability_zone']: 
                zone, created = AvailabilityZone.objects.get_or_create(code=row['availability_zone'])
                site.availability_zone = zone
                self.stdout.write("availability_zone = "+row['availability_zone'])
                #print zone.pk

            if row['street'] or row['city'] or row['state'] or row['country']:
                address, created = SiteAddress.objects.get_or_create(street=row['street'], city=row['city'], state=row['state'], country=row['country'], postal_code=row['postal_code'])
                site.location = address
            
            if row['region']:
                region, created = Region.objects.get_or_create(code=row['region'])
                if created: 
                    site.region = region
                    self.stdout.write( "region = "+row['region'])

            if row['provider']:
                provider, created = ColoProvider.objects.get_or_create(name=row['provider'], portal_url="", gibd_owner="", pmt_owner="")
                if created:
                    provider.save()
                provider.site.add(site)
            site.save()
            self.process_service_type(row['service'], site)
            self.stdout.write( "==========================" )

    def process_service_type(self, service_types, site):
        #split and add site to each of these
        if service_types:
            self.stdout.write("service_types")
            self.stdout.write(service_types)
            for t in service_types.split(','):
                self.stdout.write(t)
                this_type, created = Service.objects.get_or_create(name=t)
                this_type.sites.add(site)
