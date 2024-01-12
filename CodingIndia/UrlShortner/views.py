from django.shortcuts import render, redirect
from .models import ShortenedURL
import random
import string


# Create your views here.
from django.contrib.auth.decorators import login_required
def UrlShortnewView(request):
    print("Hello")
    try:
        shorturls = ShortenedURL.objects.filter(foruser=request.user.username)
        print("ShortUrls: ", shorturls)
    except:
        shorturls = []
        print("ShortUrls: ", shorturls)

    context = {'shorturls': shorturls}
    return render(request, 'UrlShortner/index.html', context)


from django.contrib.auth.decorators import login_required
def CreateShortUrl(request):
    print("2")
    short_url = ""
    shorturls = []
    if request.method == 'POST':
        long_url = request.POST.get('url')
        foruser = request.POST.get('foruser')

        short_key = generate_short_key()
        ShortenedURL.objects.create(long_url=long_url, short_key=short_key, foruser=foruser)
        short_url = request.build_absolute_uri('/') + short_key
        # return render(request, 'UrlShortner/index.html', {'short_url': short_url})
        
    try:
        shorturls = ShortenedURL.objects.filter(foruser=request.user)
        print("ShortUrls: ", shorturls)
    except:
        shorturls = []
    print("ShortUrls: ", shorturls)
    context = {'short_url': short_url, 'data':shorturls}
    return render(request, 'UrlShortner/index.html', context)


def redirect_to_long_url(request, short_key):
    shortened_url = ShortenedURL.objects.filter(short_key=short_key).first()
    if shortened_url:
        return redirect(shortened_url.long_url)
    return render(request, '404.html')


def generate_short_key():
    characters = string.ascii_letters + string.digits
    key_length = 6
    return ''.join(random.choice(characters) for _ in range(key_length))


from django.contrib.auth.decorators import login_required
def DeleteUrl(request, short_key):
    data = ShortenedURL.objects.get(short_key=short_key)
    data.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))