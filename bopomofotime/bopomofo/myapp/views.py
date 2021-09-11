from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from datetime import datetime, timezone

from . import models
from . import forms

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect("/")

def index(request):
    context = {
                "title":"Bopomofo Time!",
            }
    return render(request, "index.html", context=context)

def studypage(request):
    context = {
            "title": "Study Page",
            }
    return render(request, "studypage.html", context=context)

def mixandmatch(request):
    context = {
            "title": "Mix and Match",
            }
    return render(request, "mixandmatch.html", context=context)

def guesstheletter(request):
    context = {
            "title": "Guess the Letter",
            }
    return render(request, "guesstheletter.html", context=context)

def drawandcompare(request):
    context = {
            "title": "Draw and Compare",
            }
    return render(request, "drawandcompare.html", context=context)

@login_required
def page(request, page=0):
    return render(request, "index.html", context=context)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/registration.html", context=context)
