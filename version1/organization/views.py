__author__ = 'pxxgogo'
from django.shortcuts import render_to_response
from django.template import RequestContext
from organization.models import Organization
from notification.models import Notification
from activity.models import Activity



def list(request):
    pageTree = [{'url':"/organizationList",'name':"入驻组织列表"}]
    user = request.user
    organizationListAdmin = Organization.objects.filter(admin = user)
    organizationList = []
    existID = set([])
    for organization in organizationListAdmin:
        toAddOrganization = {}
        toAddOrganization['name'] = organization.name
        toAddOrganization['id'] = organization.id
        toAddOrganization['photoUrl'] = organization.photo.url
        toAddOrganization['class'] = 'management'
        toAddOrganization['state'] = '管理者'
        toAddOrganization['membersNum'] = organization.member.count()
        existID.add(toAddOrganization['id'])
        organizationList.append(toAddOrganization)
    organizationListDev = Organization.objects.filter(member = user)
    for organization in organizationListDev:
        len1 = len(existID)
        existID.add(organization.id)
        len2 = len(existID)
        if len1 == len2: continue
        toAddOrganization = {}
        toAddOrganization['name'] = organization.name
        toAddOrganization['id'] = organization.id
        toAddOrganization['photoUrl'] = organization.photo.url
        toAddOrganization['class'] = 'development'
        toAddOrganization['state'] = '参与者'
        toAddOrganization['membersNum'] = organization.member.count()
        organizationList.append(toAddOrganization)
    return render_to_response("organizationList.html",{'organizationListClass' : 'selected', 'pageName' : "入驻组织", 'pageTree':pageTree, 'organizationList' : organizationList},context_instance=RequestContext(request))

def organizationInfo(request,id):
    pageTree = [{'url':"/organizationList",'name':"入驻组织列表"}]
    organizationModel = Organization.objects.get(id = id)
    organization = {}
    organization['id'] = id
    organization['name'] = organizationModel.name
    organization['type'] = "学生会";
    organization['description'] = organizationModel.description
    organization['photoUrl'] = organizationModel.photo.url
    pageTree.append({'url' : "/organization/%s" % id, 'name' : organizationModel.name})
    administrationListModel = organizationModel.admin.all()
    memberList = []
    existID = set([])
    for admin in administrationListModel:
        toAddAdministration = {}
        toAddAdministration['class'] = "management"
        toAddAdministration['photoUrl'] = admin.photo.url
        toAddAdministration['name'] = admin.realName
        toAddAdministration['gender'] = '男'
        toAddAdministration['state'] = '管理员'
        toAddAdministration['username'] = admin.username
        existID.add(admin.id)
        memberList.append(toAddAdministration)
    membersListModel = organizationModel.member.all()
    for member in membersListModel:
        len1 = len(existID)
        existID.add(member.id)
        len2 = len(existID)
        if len1 == len2: continue
        toAddMember = {}
        toAddMember['class'] = "development"
        toAddMember['photoUrl'] = member.photo.url
        toAddMember['name'] = member.photo.url
        toAddMember['name'] = member.realName
        toAddMember['gender'] = member.gender
        toAddMember['state'] = '普通成员'
        toAddMember['username'] = member.username
        memberList.append(toAddMember)
    notificationList = Notification.objects.filter(adminOrganization = organizationModel).order_by("-publishTime")
    activitiesList = Activity.objects.filter(adminOrganization = organizationModel).order_by("-publishTime")
    eventsList = []
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
        eventsList.append(toAddEvent)
        s2 += 1
    return render_to_response("organizationInfo.html",{'organizationListClass' : 'selected', 'organization' : organization, 'pageName' : "入驻组织" , 'memberList' : memberList, 'eventsList' : eventsList, 'pageTree':pageTree}, context_instance=RequestContext(request))