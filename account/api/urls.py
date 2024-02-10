from django.urls import path
from account.api import views 
from rest_framework.authtoken.views import obtain_auth_token
# from account.api.views import MyTokenObtainPairSerializer, TokenObtainPairView


urlpatterns =[
    path('register', views.registration_view, name='regiser'),
    # path('login', obtain_auth_token, name='login'),
    path('log', views.login, name='log'),
    # path('login/token',views.obtain_jwt_token, name='token'),
    path('', views.getRoutes),
    path('refresh',views.refreshedToken)
]