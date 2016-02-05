from organization.models import Organization
from notification.models import Notification
from django.http import HttpResponseRedirect
import datetime

def addNotification(request, organizaitonID):
    organzation = Organization.objects.get(id = organizaitonID)
    notification = Notification()
    notification.adminOrganization = organzation
    notification.publisher = request.user
    now = datetime.datetime.now()
    notification.publishTime = now
    notification.content = request.POST['content']
    notification.title = request.POST['title']
    notification.TerminalDate = request.POST['TerminalDate']
    notification.type = 1
    notification.save()
    return HttpResponseRedirect("/organization/%s" % organizaitonID)



# Create your views here.
