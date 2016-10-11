__author__ = 'pxxgogo'
from django.shortcuts import render
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from organization.models import Organization
from notification.models import Notification
from activity.models import Activity


def myBillboard(request):
    if not request.user.is_active:
        return HttpResponseRedirect("/login")
    error = ""
    eventsList = []
    organizationList = Organization.objects.filter(member=request.user)
    for organization in organizationList:
        notificationList = Notification.objects.filter(adminOrganization=organization).order_by("-publishTime")
        activitiesList = Activity.objects.filter(adminOrganization=organization).order_by("-publishTime")
        len1 = len(notificationList)
        len2 = len(activitiesList)
        s1 = 0
        s2 = 0
        i = 1
        while s1 < len1 and s2 < len2:
            if notificationList[s1].publishTime > activitiesList[s2].publishTime:
                toAddEvent = {}
                toAddEvent['type'] = 'notification'
                toAddEvent['id'] = i
                i += 1
                toAddEvent['class'] = 'danger'
                toAddEvent['publishTime'] = notificationList[s1].publishTime
                toAddEvent['TerminalDate'] = notificationList[s1].TerminalDate
                toAddEvent['publisher'] = notificationList[s1].publisher.realName
                toAddEvent['content'] = notificationList[s1].content
                toAddEvent['summaryContent'] = notificationList[s1].title
                toAddEvent['notificationID'] = notificationList[s1].id
                toAddEvent['organizationName'] = organization.name
                toAddEvent['organizationID'] = organization.id
                eventsList.append(toAddEvent)
                s1 += 1
            else:
                toAddEvent = {}
                toAddEvent['type'] = 'activity'
                toAddEvent['id'] = i
                i += 1
                toAddEvent['class'] = 'success'
                toAddEvent['publishTime'] = activitiesList[s2].publishTime
                toAddEvent['TerminalDateTime'] = activitiesList[s2].date
                toAddEvent['publisher'] = activitiesList[s2].publisher.realName
                toAddEvent['content'] = activitiesList[s2].content
                toAddEvent['summaryContent'] = activitiesList[s2].name
                toAddEvent['position'] = activitiesList[s2].position
                toAddEvent['activityID'] = activitiesList[s2].id
                toAddEvent['organizationName'] = organization.name
                toAddEvent['organizationID'] = organization.id
                eventsList.append(toAddEvent)
                s2 += 1
        while s1 < len1:
            toAddEvent = {}
            toAddEvent['type'] = 'notification'
            toAddEvent['id'] = i
            i += 1
            toAddEvent['class'] = 'danger'
            toAddEvent['publishTime'] = notificationList[s1].publishTime
            toAddEvent['TerminalDate'] = notificationList[s1].TerminalDate
            toAddEvent['publisher'] = notificationList[s1].publisher.realName
            toAddEvent['content'] = notificationList[s1].content
            toAddEvent['summaryContent'] = notificationList[s1].title
            toAddEvent['notificationID'] = notificationList[s1].id
            toAddEvent['organizationName'] = organization.name
            toAddEvent['organizationID'] = organization.id
            eventsList.append(toAddEvent)
            s1 += 1
        while s2 < len2:
            toAddEvent = {}
            toAddEvent['type'] = 'activity'
            toAddEvent['id'] = i
            i += 1
            toAddEvent['class'] = 'success'
            toAddEvent['publishTime'] = activitiesList[s2].publishTime
            toAddEvent['TerminalDateTime'] = activitiesList[s2].date
            toAddEvent['publisher'] = activitiesList[s2].publisher.realName
            toAddEvent['content'] = activitiesList[s2].content
            toAddEvent['summaryContent'] = activitiesList[s2].name
            toAddEvent['position'] = activitiesList[s2].position
            toAddEvent['activityID'] = activitiesList[s2].id
            toAddEvent['organizationName'] = organization.name
            toAddEvent['organizationID'] = organization.id
            eventsList.append(toAddEvent)
            s2 += 1
    length = len(eventsList)
    for i in range(length - 1):
        for j in range(i, length):
            if eventsList[i]['publishTime'] < eventsList[j]['publishTime']:
                temp = eventsList[i]
                eventsList[i] = eventsList[j]
                eventsList[j] = temp
    pageTree = [{'url': "/myBillboard", 'name': "最新动态"}]
    return render(request, "myBillboard.html",
                  {'error': error,
                   'pageName': "最新动态",
                   'eventsList': eventsList, 'myBillboardClass': 'selected', 'pageTree': pageTree})
