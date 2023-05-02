from django.urls import path
from blogs import views

urlpatterns = [
    path("", views.index, name="blogs_index"),
    path("addblog/", views.addblog, name="addblog"),
    path("Tagsblog/<int:id>/", views.TagsBlog, name="tagsblog"),

    path('readblog/<post_id>/', views.Readblog, name="readblog"),
    path('readplay/<post_id>/', views.ReadPlay, name="readplay"),

]