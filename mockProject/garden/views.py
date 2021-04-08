from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! Welcome to my Gardening Website")

def about(request):
    return HttpResponse("About my Gardens")