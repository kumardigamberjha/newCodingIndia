from django.urls import path
from website import views


urlpatterns = [
    path("", views.index, name="web_index"),
    path("ContactUs/", views.ContactUsPage, name="contactus"),
    path("PrivacyPolicy/", views.PrivacyPolicy, name="privacypolicy"),
    path("Portfolio/", views.PortfolioPage, name="portfolio"),
    path("PortfolioDetail/<str:slug>/", views.PortfolioDetailPage, name="portfoliodetail"),


]