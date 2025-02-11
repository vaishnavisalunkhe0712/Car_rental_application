from django.http import HttpResponse


def Home1(request):
    return HttpResponse("This is bike module")
