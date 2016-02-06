from organization.models import Organization
from activity.models import Activity
from django.http import HttpResponseRedirect
import datetime

def addActivity(request, organizationID):
    organzation = Organization.objects.get(id = organizationID)
    activity = Activity()
    activity.adminOrganization = organzation
    activity.publisher = request.user
    now = datetime.datetime.now()
    activity.publishTime = now
    activity.content = request.POST['content']
    activity.name = request.POST['name']
    activity.date = request.POST['date']
    activity.position = request.POST['position']
    activity.type = 1
    activity.save()
    return HttpResponseRedirect("/organization/%s" % organizationID)

def deleteActivity(request, organizationID, activityID):
    activity = Activity.objects.get(id = activityID)
    activity.delete()
    return HttpResponseRedirect("/organization/%s" % organizationID)