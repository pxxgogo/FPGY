__author__ = 'pxxgogo'
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect



def index(request):
    if not request.user.username:
        return HttpResponseRedirect("/")
    return render_to_response("index.html",{'pageName':"首页", 'homeClass' : 'selected'},context_instance=RequestContext(request))