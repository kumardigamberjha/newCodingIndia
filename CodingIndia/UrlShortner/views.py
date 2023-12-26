from django.shortcuts import render, redirect
from .models import ShortenedURL
import random
import string

# Create your views here.
def UrlShortnewView(request):
    return render(request, 'UrlShortner/index.html')


def CreateShortUrl(request):
    short_url = ""
    if request.method == 'POST':
        long_url = request.POST.get('url')
        short_key = generate_short_key()
        ShortenedURL.objects.create(long_url=long_url, short_key=short_key)
        short_url = request.build_absolute_uri('/') + short_key
        # return render(request, 'UrlShortner/index.html', {'short_url': short_url})
    print("Hello")
    
    conext = {'short_url': short_url}
    return render(request, 'UrlShortner/index.html')


def redirect_to_long_url(request, short_key):
    shortened_url = ShortenedURL.objects.filter(short_key=short_key).first()
    if shortened_url:
        return redirect(shortened_url.long_url)
    return render(request, '404.html')


def generate_short_key():
    characters = string.ascii_letters + string.digits
    key_length = 6
    return ''.join(random.choice(characters) for _ in range(key_length))