from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('stories.html', views.stories, name="stories"),
    path('myprojects.html', views.projects, name="myprojects"),
]
