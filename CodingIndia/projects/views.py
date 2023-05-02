from django.shortcuts import render
from MyCodes.models import Codings

# Create your views here.
def index(request):
    code = Codings.objects.filter(proj=True)
    context = {'proj':code}
    return render(request, "projects/index.html", context)