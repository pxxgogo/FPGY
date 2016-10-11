
from django import forms
from django.http import HttpResponseRedirect
from account.models import AccountUser
from django.shortcuts import render
from django.template.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.hashers import make_password


# class AccountAdmin(admin.ModelAdmi):
#     fieldsets = [
#         ('username',               {'fields': ['username']}),
#         ('password',               {'fields': ['password']}),
#         ('first_name',               {'fields': ['first_name']}),
#         ('last_name',               {'fields': ['last_name']}),
#         ('email',               {'fields': ['email']}),
#         ('majority',               {'fields': ['majority']}),
#         ('is_staff',               {'fields': ['is_staff']}),
#         ('is_active',               {'fields': ['is_active']}),
#         ('last_login',               {'fields': ['last_login']}),
#         ('date_joined',               {'fields': ['date_joined']}),
#     ]
#     list_display = ('username','password','first_name','last_name','email','majority','is_staff','is_active','last_login','date_joined')


class PhotoForm(forms.Form):
    photo = forms.ImageField()

    def save(self, user, commit=True):
        user.photo = self.cleaned_data["photo"]

        if commit:
            user.save()
        return user


def register(request):
    error = ""
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        user = AccountUser()
        user.username = request.POST["username"]
        user.realName = request.POST["realName"]
        user.email = request.POST["email"]
        user.phone = request.POST["phone"]
        if request.POST["gender"] == "M":
            user.gender = "男"
        else:
            user.gender = "女"
        user.password = make_password(request.POST["password"], None, 'pbkdf2_sha256')
        user.studentID = request.POST["studentID"]
        user.personID = "#"
        if form.is_valid():
            form.save(user)
            return HttpResponseRedirect("/login")
        else:
            # assert False
            error = "信息错误！"
    c = {}
    c.update(csrf(request))
    c['error'] = error
    pageTree = [{'url': "/register", 'name': "注册页"}]
    c['pageTree'] = pageTree
    c['pageName'] = "请注册"
    return render(request, "register.html", c)

# Create your models here.

def isUsernameExist(dict):
    userList = AccountUser.objects.filter(username=dict["username"])
    if len(userList) == 0:
        return 0
    else:
        return 1


def registerOnMobile(request):
    form = PhotoForm(request.POST, request.FILES)
    user = AccountUser()
    user.username = request.POST["username"]
    user.realName = request.POST["realName"]
    user.email = request.POST["email"]
    user.phone = request.POST["phone"]
    if request.POST["gender"] == "M":
        user.gender = "男"
    else:
        user.gender = "女"
    user.password = make_password(request.POST["password"], None, 'pbkdf2_sha256')
    user.studentID = request.POST["studentID"]
    user.personID = request.POST["personID"]
    if form.is_valid():
        form.save(user)
        return 0
    else:
        return 1
