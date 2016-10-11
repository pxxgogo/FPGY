from django.contrib import admin
from activity.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('date', {'fields': ['date']}),
        ('publishTime', {'fields': ['publishTime']}),
        ('publisher', {'fields': ['publisher']}),
        ('position', {'fields': ['position']}),
        ('content', {'fields': ['content']}),
        ('adminOrganization', {'fields': ['adminOrganization']}),
        ('type', {'fields': ['type']}),
        ('groupID', {'fields': ['groupID']}),

    ]
    list_display = ('name', 'publishTime', 'date', 'position', 'content', 'adminOrganization', 'type', 'groupID')


admin.site.register(Activity, ActivityAdmin)
# Register your models here.
