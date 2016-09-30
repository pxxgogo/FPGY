from organization.models import Organization
from notification.models import Notification
from django.http import HttpResponseRedirect
import datetime

def addNotification(request, organizationID):
    organzation = Organization.objects.get(id = organizationID)
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
    return HttpResponseRedirect("/organization/%s" % organizationID)

def deleteNotification(request, organizationID, notificationID):
    notification = Notification.objects.get(id = notificationID)
    notification.delete()
    return HttpResponseRedirect("/organization/%s" % organizationID)

# Create your views here.
