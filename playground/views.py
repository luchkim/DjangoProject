from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
# response function 
def say_hello (request):
    # pull data from db, send email etc. 
    return render(request, 'hello.html', {'name': 'Luke'})
    # return HttpResponse('Hello Kim')







