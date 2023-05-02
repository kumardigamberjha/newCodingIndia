from django.urls import path
from MyCodes import views

urlpatterns = [
    path('', views.index, name="code_index"),

    # Coding
    path('coding/<int:id>/', views.Codes, name="read-codes"),
    path('coding_play/<int:id>/', views.ReadPlay, name="codes_play"),
]