from django.urls import path, re_path
from django.contrib.auth import logout
from .views import ProfileView
from . import views

from . import views




app_name ='patient'
urlpatterns = [
    
    path('', views.patient_view, name='patient'),
    path('change_locale/<str:locale>/', views.change_locale, name='change_locale'),       
    path('logout/', logout, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('groups/', views.groups, name='groups'),
    path('tests_library/', views.TestsLibraryView.as_view(), name='tests_library'),
    path('bookings/', views.bookings, name='bookings'),
    path('branches/', views.branches_view, name='branches'),
    path('requests/', views.requests_view, name='requests'),
    path('report/', views.report_view, name='report'),
     path('edit_report/', views.edit_report, name='edit_report'),
     path('create_report/', views.create_report, name='create_report'),
    



    
    
    
]
