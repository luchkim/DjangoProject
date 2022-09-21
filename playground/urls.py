
""" 
Purpose:: 
Maps URL to View functions.
"""

from django.urls import path
from . import views

#URL config module: add this to main app's urls.py config. 
urlpatterns =[
    path('hello', views.say_hello) # not calling, just pass reference no (). 
]


