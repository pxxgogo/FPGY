from django.contrib import admin
from organization.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('admin', {'fields': ['admin']}),
        ('member', {'fields': ['member']}),
        ('photo', {'fields': ['photo']}),
        ('description', {'fields': ['description']}),
        ('type', {'fields': ['type']}),
        ('groupID', {'fields': ['groupID']}),

    ]
    list_display = ('name', 'photo', 'type', 'groupID')


admin.site.register(Organization, OrganizationAdmin)
# Register your models here.
