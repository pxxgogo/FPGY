from django.contrib import admin
from account.models import AccountUser


class AccountAdmin(admin.ModelAdmin):
    fieldsets = [
        ('username', {'fields': ['username']}),
        ('password', {'fields': ['password']}),
        ('realName', {'fields': ['realName']}),
        ('gender', {'fields': ['gender']}),
        ('email', {'fields': ['email']}),
        ('studentID', {'fields': ['studentID']}),
        ('personID', {'fields': ['personID']}),
        ('is_staff', {'fields': ['is_staff']}),
        ('is_active', {'fields': ['is_active']}),
        ('last_login', {'fields': ['last_login']}),
        ('date_joined', {'fields': ['date_joined']}),
        ('photo', {'fields': ['photo']}),
    ]
    list_display = ('username','password','realName','gender','email','studentID','personID','is_staff','is_active','last_login','date_joined','photo')

admin.site.register(AccountUser,AccountAdmin)


# Register your models here.


