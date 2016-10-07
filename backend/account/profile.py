__author__ = 'pxxgogo'
from django.shortcuts import render
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password


def profile(request):
    if not request.user.is_active:
        return HttpResponseRedirect("/login")
    error = ""
    pageTree = [{'url': "/profile", 'name': "个人信息"}]
    return render(request, "profile.html",
                  {'error': error, 'pageName': "个人信息",
                   'pageTree': pageTree, 'profileClass': 'selected'})


def changeInfo(request):
    error = ""
    pageTree = [{'url': "/profile", 'name': "个人信息"}, {'url': "/changeInfo", 'name': "信息修改"}]
    return render(request, "changeInfo.html",
                  {'error': error, 'pageName': "信息修改",
                   'pageTree': pageTree, 'profileClass': 'selected'})


def infoChanged(request):
    user = request.user;
    if request.method == "POST":
        if not request.POST['realName'] == "":
            user.realName = request.POST['realName']
        if not request.POST['studentID'] == "":
            user.studentID = request.POST['studentID']
        if not request.POST['phone'] == "":
            user.phone = request.POST['phone']
        if not request.POST['email'] == "":
            user.email = request.POST['email']
        if not request.POST['major'] == "":
            user.major = request.POST['major']
        if request.POST['gender'] == 'M':
            user.gender = "男"
        else:
            user.gender = "女"
        if request.FILES:
            user.photo = request.FILES['photo']
        user.save()
    return HttpResponseRedirect("/profile")


def changePassword(request):
    error = ""
    if request.method == "POST":
        user = request.user
        username = user.username
        oldPassword = request.POST['oldPassword']
        user0 = auth.authenticate(username=username, password=oldPassword)
        if user0 is not None and user0.is_active:
            user0.password = make_password(request.POST["newPassword"], None, 'pbkdf2_sha256')
            user0.save()
            auth.login(request, user0)
            return HttpResponseRedirect("/profile")
        else:
            error = "旧密码不匹配!"
    pageTree = [{'url': "/profile", 'name': "个人信息"}, {'url': "/changePassword", 'name': "密码修改"}]
    return render(request, "changePassword.html",
                  {'error': error,
                   'pageName': "密码修改",
                   'pageTree': pageTree, 'profileClass': 'selected'},
                  )
