# -*- coding=utf-8 -*-
from django.shortcuts import render
from activity.models import Activity
from curriculum.models import Curriculum
from signInEvent.models import SignInEvent
from account.models import AccountUser
import datetime



def createSignInEvent(dict):
    groupID = dict["group_ID"]
    time = datetime.datetime.fromtimestamp(dict["time"])  #dict["time"] millseconds
    activityList = Activity.objects.filter(groupID=groupID)
    type = 0
    if len(activityList) == 0:
        currculumList = Curriculum.objects.filter(groupID=groupID)
        if len(currculumList) == 0:
            return 1, 0
        type = 1
    event = SignInEvent()
    event.type = type
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




# Create your views here.
