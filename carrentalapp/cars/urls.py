from django.contrib import admin
from django.urls import include, path
from cars import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('',views.Home, name='Home'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



