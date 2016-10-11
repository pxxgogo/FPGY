from django.contrib import admin
from curriculum.models import Curriculum


class CurriculumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('time', {'fields': ['time']}),
        ('position', {'fields': ['position']}),
        ('content', {'fields': ['content']}),
        ('type', {'fields': ['type']}),
        ('groupID', {'fields': ['groupID']}),
        ('teacher', {'fields': ['teacher']}),
        ('student', {'fields': ['student']}),

    ]
    list_display = ('name', 'time', 'position', 'content', 'type', 'groupID')


admin.site.register(Curriculum, CurriculumAdmin)
# Register your models here.
