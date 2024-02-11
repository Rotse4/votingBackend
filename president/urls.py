from django.urls import path
from . import views

urlpatterns = [
    path('vote/<str:pk>', views.vote),  
    path('schoolRep', views.reps), 
    path('presidents', views.pesidents),
    path('womenRep', views.wemenRep),
    path('menRep', views.menRep),
]

