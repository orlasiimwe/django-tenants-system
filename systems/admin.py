from django.contrib import admin
from .models import Tenant

class TenantAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name","temperature","date","id_no")

admin.site.register(Tenant,TenantAdmin)
