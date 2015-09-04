from django.forms import ModelForm, Form, FileField
from reporting.models import Site

class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ['code', 'agile_no', 'project_name',  'location']

class ExcelForm(Form):
    file = FileField()
