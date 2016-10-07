__author__ = 'pxxgogo'
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.username:
        return HttpResponseRedirect("/")
    return render(request, "index.html",
                  {'pageName': "首页",
                   'homeClass': 'selected'})
