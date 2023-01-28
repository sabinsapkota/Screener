from django.urls import path
from . import views
import datetime
import threading
from .models import Crypto


app_name = 'search'
urlpatterns = [
    path("",views.search, name = 'search'),
    #path("results",views.results, name = 'results')
]


def printit():
  threading.Timer(1.0, printit).start()
  minute = datetime.datetime.now().minute
  second = datetime.datetime.now().second
  
  if minute == 14 and second == 50 or minute == 29 and second == 50 or minute == 44 and second == 50 or minute == 59 and second == 50:
   views.update()

printit()
