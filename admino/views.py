from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def admin_dash(request):
    return render(request, 'admino/admin_dash.html')


def bookings(request, booking_id):
    context = {'booking_id': booking_id}
    return render(request, 'admino/bookings.html', context)


def change_locale(request, locale):
    request.session[translation.LANGUAGE_SESSION_KEY] = locale
    return redirect('home')



def logout_view(request):
    logout(request)
    return redirect('home')


def profile_edit_view(request):
    return render(request, 'admino/profile_edit.html')

# views.py



def groups_view(request):
    groups = Group.objects.all()
    return render(request, 'admino/groups.html', {'groups': groups})

def reports_view(request):
    return render(request, 'admino/reports.html')
def branches_view(request):
    return render(request, 'admino/branches.html')
def tests_view(request):
    return render(request, 'admino/tests.html')


def doctors_view(request):
    return render(request, 'admino/doctors.html')


def prices_view(request):
    return render(request, 'admino/prices.html')


def tests_prices(request):
    return render(request, 'admino/tests_prices.html')



def contracts(request):
    return render(request, 'admino/contracts.html')



def patients_view(request):
    return render(request, 'admino/patients.html')

def bookings(request):
    return render(request, 'admino/bookings.html')
def chat_view(request):
    return render(request, 'admino/chat.html')
def accounting_link(request):
    return render(request, 'admino/accounting_link.html')

def expense_categories(request):
    return render(request, 'admino/expense_categories.html')


def expenses(request):
    return render(request, 'admino/expenses.html')



def accounting_reports(request):
    return render(request, 'admino/accounting_reports.html')



def accounting_doctor_reports(request):
    return render(request, 'admino/accounting_doctor_reports.html')

def roles_view(request):
    return render(request, 'admino/roles.html')

def users_view(request):
    return render(request, 'users.html', {})
def settings_view(request):
    return render(request, 'admino/settings.html')

def translations(request):
    return render(request, 'admino/translations.html')
def activity_logs(request):
    return render(request, 'admino/activity_logs.html')



class BackupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admino/backups.html')
    
    
    

def display_chat(request):
   return render(request, 'admino/chat.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('home')
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})






