from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User

from django.contrib import messages
from website.models import Quotes, Team, ServicesModel
import requests,random
from django.views.decorators.cache import cache_page

######################## Views ##################################
@cache_page(60 * 15)
def index(request):
    team = Team.objects.all()

    url = "https://famous-quotes4.p.rapidapi.com/random"

    querystring = {"category":[
        'motivational', 'power', 'strength', 
        'success', 'trust', 'teacher', 'science', 'technology', 
        'poetry', 'money', 'work'
    ],"count":"1"}

    headers = {
        "X-RapidAPI-Key": "c1115554d0msh7e07b79a939d0f3p1699e5jsnc633e1638385",
        "X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    # print("DATA: ", data)
    text = data[0]['text']
    author = data[0]['author']
    context = {'team': team, 'text':text, 'author': author}
    return render(request, "website/index.html", context)


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
