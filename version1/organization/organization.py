__author__ = 'pxxgogo'
from django.shortcuts import render_to_response
from django.template import RequestContext



def list(request):
    pageTree = [{'url':"/login",'name':"入驻组织列表"}]
    return render_to_response("organizationList.html",{'pageName' :"入驻组织",'pageTree':pageTree},context_instance=RequestContext(request))