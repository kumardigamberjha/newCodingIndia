from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ContactUsForm
from django.contrib.auth.models import User

from django.contrib import messages
from website.models import Quotes, Team, ServicesModel, ContactUs, Portfolio
import requests,random
from django.core.paginator import Paginator

# from django.views.decorators.cache import cache_page

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



def PortfolioPage(request):
    data = Portfolio.objects.all()
    paginator = Paginator(data, 1)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj}
    return render(request, 'website/portfolio.html', context)


def PortfolioDetailPage(request, slug):
    data = Portfolio.objects.get(slug=slug)

    context = {'data': data}
    return render(request, 'website/portfolioproject.html', context)