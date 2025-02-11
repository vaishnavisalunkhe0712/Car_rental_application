from django.contrib import admin
from django.urls import include, path
from bicycle import views


urlpatterns = [
   
   path('',views.Home2, name='Home2')
   
]
