from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('download/<int:document_id>/', views.download_word, name='download_word'),
]