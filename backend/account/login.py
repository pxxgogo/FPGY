__author__ = 'pxxgogo'
from django.shortcuts import render
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from account.register import isUsernameExist
import string
import random


def login(request):
    if request.user.is_active:
        return HttpResponseRedirect("/profile")
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/profile")
        else:
            error = "登陆失败"
    pageTree = [{'url': "/login", 'name': "登陆页"}]
    return render(request, "login.html",
                              {'error': error,
                               'pageName': "请登陆", 'pageTree': pageTree})


def logInOnMobile(dict):
    user = auth.authenticate(username=dict["username"], password=dict["password"])
    if user is not None and user.is_active:
        if user.mobileOn == True:
            if dict["force_flag"] == 0:
                return 3, {}
        accountData = {}
        accountData["username"] = dict["username"]
        accountData["real_name"] = user.realName
        accountData["gender"] = user.gender
        accountData["email"] = user.email
        accountData["student_ID"] = user.studentID
        accountData["person_ID"] = user.personID
        accountData["photo"] = user.photo.url
        accountData["mobile_on_flag"] = True
        accountData["mobile_token"] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        user.mobileOn = True
        user.mobileToken = accountData["mobile_token"]
        user.save()
        return 0, accountData
    else:
        flag = isUsernameExist(dict)
        if flag == 0:
            return 1, {}
        else:
            return 2, {}