from django.contrib import admin
from django.urls import include, path
from bike import views


urlpatterns = [
   
   path('',views.Home1, name='Home1')
   
]
