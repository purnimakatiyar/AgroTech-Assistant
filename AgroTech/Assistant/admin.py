from django.contrib import admin
from Assistant.models import Sgn
from Assistant.models import Suppsgn,SupplierOrder

# Register your models here.
admin.site.register(Sgn)
admin.site.register(Suppsgn)
admin.site.register(SupplierOrder)
