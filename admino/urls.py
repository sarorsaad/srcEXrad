from django.urls import path
from . import views
from .views import prices_view
from .views import patients_view
from .views import accounting_link
from django.contrib.auth import views as auth_views

app_name ='admino'
urlpatterns = [
    path('admin_dash/', views.admin_dash, name='admin_dash'),
    path('bookings/<int:booking_id>/', views.bookings, name='bookings'),
    path('change-locale/<str:locale>/', views.change_locale, name='change_locale'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('groups/', views.groups_view, name='groups'),
    path('reports/', views.reports_view, name='reports'),
    path('branches/', views.branches_view, name='branches'),
    path('tests/', views.tests_view, name='tests'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('prices/', prices_view, name='prices_link'),
    path('tests_prices/', views.tests_prices, name='tests_prices'),
    path('contracts/', views.contracts, name='contracts'),
    path('patients/', patients_view, name='patients'),
    path('bookings/', views.bookings, name='bookings'),
    path('chat/', views.chat_view, name='chat'),
    path('accounting_link/', accounting_link, name='accounting_link'),
    path('expense_categories/', views.expense_categories, name='expense_categories'),
    path('expenses/', views.expenses, name='expenses'),
    path('accounting_reports/', views.accounting_reports, name='accounting_reports'),
    path('accounting_doctor_reports/', views.accounting_doctor_reports, name='accounting_doctor_reports'),
    path('roles/', views.roles_view, name='roles'),
    path('users/', views.users_view, name='users'),
    path('settings/', views.settings_view, name='settings'),
    path('translations/', views.translations, name='translations'),
    path('activity_logs/', views.activity_logs, name='activity_logs'),
    path('backups/', views.BackupView.as_view(), name='backups'),
    path('display_chat/', views.display_chat, name='display_chat'),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),





  
]

    
   

