from django.contrib import admin
from activity.models import Activity

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name',               {'fields': ['name']}),
        ('date',              {'fields': ['date']}),
        ('planNum',             {'fields': ['planNum']}),
        ('currentNum',              {'fields': ['currentNum']}),
        ('position',            {'fields': ['position']}),
        ('summaryContent',            {'fields': ['summaryContent']}),
        ('info',            {'fields': ['info']}),
        ('ddl',            {'fields': ['ddl']}),
        ('adminOrganization',            {'fields': ['adminOrganization']}),
        ('participant',            {'fields': ['participant']}),
        ('inDate',            {'fields': ['inDate']}),
    ]
    list_display = ('name','date','planNum','currentNum','position','summaryContent','info','ddl','adminOrganization','inDate')

admin.site.register(Activity, ActivityAdmin)
# Register your models here.

