from django.contrib import admin
from signInEvent.models import SignInEvent


class SignInEventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('time', {'fields': ['time']}),
        ('type', {'fields': ['type']}),
        ('groupID', {'fields': ['groupID']}),
        ('participant', {'fields': ['participant']}),

    ]
    list_display = ('time', 'type', 'groupID')


admin.site.register(SignInEvent, SignInEventAdmin)
