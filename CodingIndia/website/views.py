from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ContactUsForm
from django.contrib.auth.models import User

from django.contrib import messages
from website.models import Quotes, Team, ServicesModel, ContactUs
import requests,random
from django.views.decorators.cache import cache_page

######################## Views ##################################
# @cache_page(60 * 15)
def index(request):
    team = Team.objects.all()

    context = {'team': team}
    return render(request, "website/index.html", context)


def PrivacyPolicy(request):
    return render(request, 'website/privacypolicy.html')

def ContactUsPage(request):
    form = ContactUsForm()
    service = ServicesModel.objects.all()
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
        else:
            print("Form Error: ", form.errors)
    context = {'form': form, 'service': service}
    return render(request, 'website/contactus.html', context)
