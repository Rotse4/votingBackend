from django.urls import path
from . import views

urlpatterns = [
    path('vote/<str:pk>', views.vote),  
]

