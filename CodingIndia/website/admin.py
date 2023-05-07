from django.contrib import admin
from website.models import Quotes, Team, ServicesModel, ContactUs

# Register your models here.

admin.site.register(Quotes)
admin.site.register(Team)
admin.site.register(ServicesModel)
admin.site.register(ContactUs)
