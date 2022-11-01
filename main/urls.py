from django.urls import path, include
from main.views import index,about




urlpatterns = [
    path("", index,name="index"),
    path("about/",about,name="about")
]




