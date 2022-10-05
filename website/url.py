from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('con',views.con),
    path('sgn',views.sgn),
    path('abs',views.abs),
     path('crs',views.crs),
]
