from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def specs_th(arg):
    data = '<tr>'
    data += '<th>&nbsp;</th>'
    data += '<th>S</th>'
    data += '<th>P</th>'
    data += '<th>E</th>'
    data += '<th>C</th>'
    data += '<th>S</th>'
    data += '</tr>'
    return mark_safe(data)

@register.filter
def specs_coloprovider_tr(coloprovider):
    data = '<tr>'
    data += '<td>'+str(coloprovider)+'</td>'
    data += '<td class="'+str(coloprovider.get_grade('security'))+'"></td>'
    data += '<td class="'+str(coloprovider.get_grade('price'))+'"></td>'
    data += '<td class="'+str(coloprovider.get_grade('contract'))+'"></td>'
    data += '<td class="'+str(coloprovider.get_grade('engineering'))+'"></td>'
    data += '<td class="'+str(coloprovider.get_grade('scale'))+'"></td>'
    data += '</tr>'
    return mark_safe(data)

@register.filter
def specs_site_tr(site):
    data = '<tr>'
    data += '<td><a href="'+site.get_absolute_url()+'">'+str(site)+'</a></td>'
    data += '<td class="'+str(site.get_grade('security'))+'"></td>'
    data += '<td class="'+str(site.get_grade('price'))+'"></td>'
    data += '<td class="'+str(site.get_grade('contract'))+'"></td>'
    data += '<td class="'+str(site.get_grade('engineering'))+'"></td>'
    data += '<td class="'+str(site.get_grade('scale'))+'"></td>'
    data += '</tr>'
    return mark_safe(data)
