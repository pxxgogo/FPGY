from django.contrib import admin
from notification.models import Notification

class NotificationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('publishTime',            {'fields': ['publishTime']}),
        ('TerminalDate',            {'fields': ['TerminalDate']}),
        ('publisher',            {'fields': ['publisher']}),
        ('title',            {'fields': ['title']}),
        ('content',            {'fields': ['content']}),
        ('adminOrganization',            {'fields': ['adminOrganization']}),
        ('type',            {'fields': ['type']}),
    ]
    list_display = ('title','content','publishTime','TerminalDate','adminOrganization','type')

admin.site.register(Notification, NotificationAdmin)
# Register your models here.

