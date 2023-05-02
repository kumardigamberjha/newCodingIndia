from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect

from MyCodes.models import Category, Codings

def index(request):
    code = Codings.objects.all()
    play = Category.objects.all()

    context = {"code": code, "play":play}
    return render(request, "MyCodes/code_index.html", context)

code_cat = 0
def ReadPlay(request, id):
    if request.method == "GET":
        plays = Category.objects.get(pk = id)
        global code_cat
        code_cat = id
        blogs = Codings.objects.filter(cat=plays)
        read = {'blogs':blogs, 'play':plays}
        # return JsonResponse()
    return render(request, "MyCodes/codes_play.html", read)


def Codes(request, id= None):
    sel_code = Codings.objects.get(id = id)
    code = Codings.objects.all()
    context = {"coding": code, "sel_code": sel_code,"play_id": code_cat}
    return render(request, "MyCodes/hps.html", context)
    

