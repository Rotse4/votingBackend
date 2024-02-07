from django.urls import path
from . import views

urlpatterns = [
    path('pres', views.registration),
    path('vote/<str:pk>', views.vote),
]

