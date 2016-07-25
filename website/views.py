from django.http import HttpResponse

def home(request):
    text = "<h1>Welcome to the homepage of this website"
    return HttpResponse(text)