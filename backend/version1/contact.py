__author__ = 'pxxgogo'
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def contact(request):
    pageTree = [{'url': "/contact", 'name': "联系我"}]
    return render_to_response("contact.html",
                              {'csrf_token': request.COOKIES['csrftoken'], 'user': request.user, 'pageName': "联系我",
                               'pageTree': pageTree, 'contactClass': 'selected'})
