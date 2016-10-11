__author__ = 'pxxgogo'
from django.http import JsonResponse
from account.register import isUsernameExist, registerOnMobile
from account.login import logInOnMobile
from account.logout import logOutOnMobile
from signInEvent.views import createSignInEvent, signIn
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api(request):
    if request.method == 'POST':
        type = request.POST.get("type", "")
        if type == "username_availability":
            returnCode = isUsernameExist(request.POST)
            return JsonResponse({"return_code": returnCode}, safe=False)

        if type == "register":
            returnCode = registerOnMobile(request)
            return JsonResponse({"return_code": returnCode}, safe=False)

        if type == "log_in":
            returnCode, accountData = logInOnMobile(request.POST)
            return JsonResponse({"return_code": returnCode, "account_data": accountData}, safe=False)

        if type == "log_out":
            returnCode = logOutOnMobile(request.POST)
            return JsonResponse({"return_code": returnCode}, safe=False)

        if type == "create_sign_in_event":
            returnCode, eventID = createSignInEvent(request.POST)
            return JsonResponse({"return_code": returnCode, 'event_id': eventID}, safe=False)

        if type == "sign_in":
            returnCode = signIn(request.POST)
            return JsonResponse({"return_code": returnCode}, safe=False)













