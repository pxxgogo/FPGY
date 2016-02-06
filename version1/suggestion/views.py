from django.http import HttpResponseRedirect
from suggestion.models import Suggestion
import datetime


def submitSuggestion(request):
    suggestion = Suggestion()
    if request.method == "POST":
        suggestion.adviser = request.POST['adviser']
        suggestion.content = request.POST['content']
        suggestion.email = request.POST['email']
        suggestion.subject = request.POST['subject']
        now = datetime.datetime.now()
        suggestion.time = now
        suggestion.save()
        return HttpResponseRedirect("")
    return HttpResponseRedirect("/")




# Create your views here.
