from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path("index",views.index,name='index'),
    path("house",views.index1,name='house'),
    path("factory",views.index2,name='factory'),
    path("vastuhindi",views.index3,name='vastuhindi'),
    path("househindi",views.index4,name='househindi'),
    path("about",views.index5,name='about'),
    path("abouthindi",views.index6,name='abouthindi'),
    path("factoryhindi",views.index7,name='factoryhindi'),
    path("hospital",views.index8,name='hospital'),
    path("hospitalhindi",views.index9,name='hospitalhindi'),
    path("shopvastu",views.index10,name='shopvastu'),
    path("shophindi",views.index11,name='shophindi'),
    path("office",views.index12,name='office'),
    path("officehindi",views.index13,name='officehindi'),
    path("warehouse",views.index14,name='warehouse'),
    path("warehousehindi",views.index15,name='warehousehindi'),
    path("vastutips",views.index16,name='vastutips'),
    path("vastutipshindi",views.index17,name='vastutipshindi')
    
]