from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="img_home"),
    path('request/', views.import_image, name="img_import"),


]
