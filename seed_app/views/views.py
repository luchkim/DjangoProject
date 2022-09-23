from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def homePage(request):
    return HttpResponse("Hello World")
    # return render()

