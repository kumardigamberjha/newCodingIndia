from django.urls import path
from GenAI import views

urlpatterns = [
    path('', views.GenIntro, name="genintro"),
    path('GenAIConversation/', views.GenAIConversation, name="genaiconversation"),

]