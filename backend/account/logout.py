from django.contrib import auth
from django.http import HttpResponseRedirect
from account.models import AccountUser


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/login")


def logOutOnMobile(dict):
    mobile_token = dict["mobile_token"]
    userList = AccountUser.objects.filter(username=dict["username"])
    if not len(userList) == 1:
        return 1
    user = userList[0]
    if mobile_token == user.mobileToken:
        user.mobileToken = ""
        user.mobileOn = False
        return 0
    else:
        return 1
