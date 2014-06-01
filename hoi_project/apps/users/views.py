from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

# User Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')