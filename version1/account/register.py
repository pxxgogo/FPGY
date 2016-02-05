from django import forms
from django.http import HttpResponseRedirect
from account.models import AccountUser
from django.shortcuts import render_to_response
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


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    realName = forms.CharField()
    phone = forms.CharField()
    major = forms.CharField()
    photo = forms.ImageField()
    password = forms.CharField()
    studentID = forms.CharField()
    gender = forms.CharField()

    def save(self, commit=True):
        user = AccountUser();
        user.username = self.cleaned_data["username"]
        user.realName = self.cleaned_data["realName"]
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]
        user.major = self.cleaned_data["major"]
        user.photo = self.cleaned_data["photo"]
        if self.cleaned_data["gender"] == "M":
            user.gender = "男"
        else:
            user.gender = "女"
        user.password = make_password(self.cleaned_data["password"], None, 'pbkdf2_sha256')
        user.studentID = self.cleaned_data["studentID"]
        if commit:
            user.save()
        return user
    # def __init__(self,Dict,Files):
    #     forms.Form.__init__(self)
    #     self.username = Dict['username']
    #     self.email = Dict['email']
    #     self.major = Dict['major']
    #     self.password = Dict['password']
    #     self.phone = Dict['password']
    #     self.realName = Dict['realName']
    #     self.photo = Files['photo']

def register(request):
    error = ""
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login")
        else:
            # assert False
            error = "信息错误！"
    c = {}
    c.update(csrf(request))
    c['error'] = error
    pageTree = [{'url':"/register",'name':"注册页"}]
    c['pageTree'] = pageTree
    c['pageName'] = "请注册"
    return render_to_response("register.html", c,context_instance=RequestContext(request))
# Create your models here.
