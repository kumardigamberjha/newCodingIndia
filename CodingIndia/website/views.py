from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ContactUsForm, NewsLetterForm
from django.contrib.auth.models import User

from django.contrib import messages
from website.models import Quotes, Team, ServicesModel, ContactUs, Portfolio, NewsLetter
import requests,random
from django.core.paginator import Paginator
from django.core.mail import send_mail

from CodingIndia.settings import EMAIL_HOST_USER

# from django.views.decorators.cache import cache_page

######################## Views ##################################
# @cache_page(60 * 15)
def index(request):
    team = Team.objects.all()
    port = Portfolio.objects.all()[:4]
    context = {'team': team, 'port':port}
    return render(request, "website/index.html", context)


def AboutUs(request):
    data = "Coding India"
    context = {'data': data}
    return render(request, 'website/about.html', context)


def PrivacyPolicy(request):
    return render(request, 'website/privacypolicy.html')


def ContactUsPage(request):
    form = ContactUsForm()
    service = ServicesModel.objects.all()
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        name = request.POST.get('fname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if form.is_valid():
            form.save()
            send_mail("Coding India: Contact Us", f"New mail from the user: {name} by email: {email}. \n The message is:\n{message}", EMAIL_HOST_USER, [email], fail_silently=True) 
            messages.success(request, 'Message Sent Successfully')
            # print("Form Saved")
        else:
            messages.success(request, 'Something went wrong')

            # print("Form Error: ", form.errors)
    context = {'form': form, 'service': service}
    return render(request, 'website/contactus.html', context)



def NewsletterFormPage(request):
    form = NewsLetterForm()
    if request.method == "POST":
        form = NewsLetterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Subscribed Successfully')

            # print("Form Saved")
        else:
            # print("Form Error: ", form.errors)
            messages.success(request, 'Failed to Subscribed Successfully')

    context = {'form': form}
    return redirect('/')


def PortfolioPage(request):
    data = Portfolio.objects.all()
    paginator = Paginator(data, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj}
    return render(request, 'website/portfolio.html', context)


def PortfolioDetailPage(request, slug):
    data = Portfolio.objects.get(slug=slug)

    context = {'data': data}
    return render(request, 'website/portfolioproject.html', context)