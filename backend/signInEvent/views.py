# -*- coding=utf-8 -*-
from django.shortcuts import render
from activity.models import Activity
from organization.models import Organization
from curriculum.models import Curriculum
from signInEvent.models import SignInEvent
from account.models import AccountUser
import datetime
import calendar


def createSignInEvent(dict):
    groupID = dict["group_ID"]
    time = datetime.datetime.fromtimestamp(dict["time"])  #dict["time"] millseconds
    organizationList = Organization.objects.filter(groupID=groupID)
    type = 0
    if len(organizationList) == 0:
        currculumList = Curriculum.objects.filter(groupID=groupID)
        if len(currculumList) == 0:
            return 1, 0
        type = 1
    event = SignInEvent()
    event.type = type  # 0表示组织者活动，1表示课程
    if event.type == 0:
        event.activity = Activity.objects.get(id=dict["activity_ID"])
    event.groupID = groupID
    event.time = time
    event.save()
    return 0, event.id

def signIn(dict):
    eventID = dict["event_ID"]
    personID = dict["persion_ID"]
    event = SignInEvent.objects.get(id=eventID)
    event.participant.add(AccountUser.objects.get(personID))
    return 0

def showSignInEvents(dict):
    groupID = dict["group_ID"]
    eventList = SignInEvent.objects.filter(groupID=groupID).order_by("-time")
    resultList = []
    for event in eventList:
        result = {}
        result["time"] = calendar.timegm(event.time.timetuple())
        result["participants_num"] = event.participant.count()
        if event.type == 0:
            result["activity_name"] = event.activity.name
            result["activity_ID"] = event.activity.id
            result["total_people_num"] = Organization.objects.get(groupID=groupID).member.count()
        else:
            result["total_people_num"] = Curriculum.objects.get(groupID=groupID).student.count()
        resultList.append(result)
    return 0, resultList


# Create your views here.
