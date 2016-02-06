from django.contrib import admin
from suggestion.models import Suggestion
class SuggestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('adviser',               {'fields': ['adviser']}),
        ('subject',            {'fields': ['subject']}),
        ('time',              {'fields': ['time']}),
        ('email',              {'fields': ['email']}),
        ('content',            {'fields': ['content']}),
    ]
    list_display = ('adviser','subject','time','email','content')

admin.site.register(Suggestion, SuggestionAdmin)
# Register your models here.
