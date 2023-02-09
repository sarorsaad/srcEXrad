from django.shortcuts import render, redirect
from django.contrib import staticfiles
from django.contrib.auth import logout
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound
import logging

app_name = 'patient'

def patient_view(request):
    return render(request, 'patient/patient.html')

def change_locale(request, locale):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('preferred_language', locale)
    return response

class ProfileView(TemplateView):
    template_name = 'patient/profile.html'

def groups(request):
    return render(request, 'patient/groups.html')

class TestsLibraryView(TemplateView):
    template_name = 'patient/tests_library.html'

def bookings(request):
    return render(request, 'patient/bookings.html', {})

def branches_view(request):
    return render(request, 'patient/branches.html')

def requests_view(request):
    return render(request, 'patient/requests.html')

def report_view(request):
    return render(request, 'patient/report.html')

def edit_report(request):
    # logic for handling the request and returning the response
    return HttpResponse("edit_report view")

def create_report(request):
    return render(request, 'patient/create_report.html')


logger = logging.getLogger(__name__)

def my_view(request):
    # some code
    try:
        static_file = staticfiles.static('path/to/static/file.css')
    except Exception as e:
        logger.warning(f"Static file not found: {e}")
        return HttpResponseNotFound('Static file not found')
    # some code
    return HttpResponse('Static file found')
