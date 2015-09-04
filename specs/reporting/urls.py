from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', login_required(TemplateView.as_view(template_name="reporting/home.html")), name="home"),
    #Summary pages 
    url(r'^upload/$', views.upload_excel, name="upload"),
    url(r'^summary/topology/$', views.topology_summary, name="topology_summary"),
    url(r'^summary/regional/$', views.RegionList.as_view(), name="regional_summary"),
    url(r'^summary/vendors/$', views.ColoProviderList.as_view(), name="vendors_summary"),
    url(r'^summary/sites/$', views.sites_summary, name="sites_summary"),
    #Listings
    url(r'^list/sites/$', views.SiteList.as_view(), name="sites_list"),
    #url(r'^list/weights/$', views.SpecsWeightsList.as_view(), name="spec_weights_list"),
    #detail pages
    url(r'^detail/site/(?P<site_id>[0-9]+)/$', views.site_detail, name='site'),
    url(r'^detail/site/(?P<site_code>[A-Z]+[0-9]+)/$', views.site_by_code, name='site_by_code'),
    url(r'^detail/site/(?P<site_code>[A-Z]+[0-9]+)/(?P<specs_id>[0-9]+)/$', views.specs_by_site_code_and_pk, name='specs_by_site_code_and_pk'),
]
