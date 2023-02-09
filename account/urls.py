from django.urls import path
from . import views
from .views import LoginAdminView
from .views import LoginUserView



app_name ='account'
urlpatterns = [
   
    path('', views.create_account_view, name='create_account'),
    path('register_submit/', views.register_submit, name='register_submit'),
    path('admin_login/', LoginAdminView.as_view(), name='Login_Admin'),
     path('user_login/', LoginUserView.as_view(), name='Login_User'),
     path('register_success/', views.register_success, name='register_success'),



  
]
