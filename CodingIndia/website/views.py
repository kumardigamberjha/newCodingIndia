from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User

from django.contrib import messages
from website.models import Quotes, Team

######################## Views ##################################
def index(request):
    user = User.objects.all()
    team = Team.objects.all()
    quotes = Quotes.objects.all()
    context = {'quotes': quotes, 'team': team,"user": user}
    return render(request, "website/index.html", context)

