from django.contrib import admin
from django.urls import path
#! import views
from . import views

urlpatterns = [
    path("",views.index,name='index_page'),
    path("runcode",views.runcode,name='runcode'),
]
