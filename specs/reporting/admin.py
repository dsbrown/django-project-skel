from django.contrib import admin
from .models import *

admin.site.register(Region)
admin.site.register(AvailabilityZone)
admin.site.register(ColoProvider)
admin.site.register(Site)
admin.site.register(SiteAddress)
admin.site.register(Specs)
admin.site.register(Security)
admin.site.register(Price)
admin.site.register(Engineering)
admin.site.register(Contract)
admin.site.register(Scale)
admin.site.register(SpecsWeights)
admin.site.register(Service)
admin.site.register(SecurityWeights)
admin.site.register(PriceWeights)
admin.site.register(EngineeringWeights)
admin.site.register(ContractWeights)
admin.site.register(ScaleWeights)