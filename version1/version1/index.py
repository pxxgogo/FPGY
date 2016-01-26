__author__ = 'pxxgogo'
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response("index.html",{'pageName':"首页"},context_instance=RequestContext(request))