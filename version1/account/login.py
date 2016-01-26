__author__ = 'pxxgogo'
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect


def login(request):
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
            auth.login(request, user)
        # Redirect to a success page.
            return HttpResponseRedirect("/")
        else:
            error = "登陆失败"

    # else:
    #     # Show an error page
    #     return HttpResponseRedirect("/login")
    pageTree = [{'url':"/login",'name':"登陆页"}]
    return render_to_response("login.html",{'error':error,'pageName':"请登陆",'pageTree':pageTree},context_instance=RequestContext(request))