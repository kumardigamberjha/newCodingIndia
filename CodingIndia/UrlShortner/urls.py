from django.urls import path
from . import views

urlpatterns = [
    path('', views.UrlShortnewView, name="urlshortner"),
    path('CreateShortUrl/', views.CreateShortUrl, name="createshorturl"),
    path('<str:short_key>/', views.redirect_to_long_url, name='redirect_to_long_url'),
    path('Delete/<str:short_key>/', views.DeleteUrl, name='deleteurl'),

]