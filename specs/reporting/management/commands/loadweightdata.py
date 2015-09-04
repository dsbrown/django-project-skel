###################################################################################
#                     Django Management Command loadweightdata
#
# Description:
#     Takes Excel spreadsheets with the scaling weights in the format, column header, 
#     then value in the next row, same column:
#
#         date            account_management      contact_list
#         8/27/15 11:18   0.930%                  5.294%
#
#     and writes it into the appropriate table. The program is invoked as:
#
#     %python manage.py loadweightdata --path /path/to/the/spread/sheets/ContractWeights.xlsx --table ContractWeights
#
#     etc.
# Author: David S. Brown
# v1.0  DSB     26 Aug 2015     Original program
#
####################################################################################

from django.core.management.base import BaseCommand, CommandError
from reporting.models import ContractWeights, EngineeringWeights, PriceWeights, ScaleWeights, SecurityWeights, SpecsWeights
from os.path import isfile, join, splitext
from openpyxl import load_workbook
from django.apps import apps 
VALID_TABLES = ('ContractWeights', 'EngineeringWeights', 'PriceWeights', 'ScaleWeights', 'SecurityWeights', 'SpecsWeights',)
SUPPORTED_FORMATS = ('.xlsx', '.xlsm', '.xltx', '.xltm')

class Command(BaseCommand):
    help = 'Loads the score weight tables'

    def add_arguments(self, parser):
        parser.add_argument("--path", nargs="?", dest="path", required=True, 
                    help="Path to excel file")

        parser.add_argument("--table", nargs="?", dest="table", required=True, 
                    help="Name of table to write to")

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
        table = options['table']
        #check if file is valid before continuing
        if self.valid_excel_file(path):
            #self.stdout.write('Processing file - %s' % path) 
            if table in VALID_TABLES:
                self.parse(path,table)
            else:
                raise CommandError('Table "%s" is not a valid table' % table)
        else:
            raise CommandError('Path "%s" is not a valid excel file' % path)

    def get_rows_fmt(self,ws):
        headers=[0]
        first_row = True
        rows = []
        for row in ws.rows:
            c = 0
            t = {}
            for cell in row:
                if first_row:                  
                    h=str(cell.value)
                    if isinstance(h,str):  # I am having a problem detecting empty columns here
                        headers[0]+=1
                        h = h.lower()      # all columns in the model are lower case!
                        h = h.strip()      # remove extra spaces begining and end
                        headers.append(h)
                    else:
                        headers.append(False)
                    #self.stdout.write('Column Header [%s]'%h)
                else:
                    c += 1
                    if headers[c] != False:
                        t[headers[c]] = cell.value
            if first_row:
                #print headers
                first_row = False
                continue
            rows.append(t)
        return rows

    def parse(self, path, table):
        #self.stdout.write('Parsing weight file %s'%table)
        table_obj = apps.get_model(app_label='reporting', model_name=table)
        wb = load_workbook(filename=path, data_only=True)
        ws = wb.worksheets[0]
        row = self.get_rows_fmt(ws)
        if row[0]:
            if table_obj.objects.count() >0: table_obj.objects.all().delete() # uniquie to weights only!
            #self.stdout.write('writing [%s]'%row[0])
            t, created = table_obj.objects.get_or_create(**row[0])
            t.save()
