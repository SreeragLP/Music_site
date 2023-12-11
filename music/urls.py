"""
URL configuration for musicsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music import views

app_name="music"

urlpatterns = [
    path('',views.home,name='home'),
    path('artist/<str:a>/', views.artist, name='artist'),
    path('albums/<str:a>/', views.albums, name='albums'),
    path('songs/<str:a>/', views.songs, name='songs'),
    #path('play/<str:a>/', views.play, name='play'),

    path('play/<int:a>/', views.play, name='play'),

    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name="logout"),




    path('playlist', views.playlist, name='playlist'),


    path('add_to_playlist/<int:a>/', views.add_to_playlist, name='add_to_playlist'),

    path('playlist_remove/<p>',views.playlist_remove,name="playlist_remove"),

    path('shuffle', views.shuffle, name='shuffle'),

    path('all_artists/', views.all_artists, name='all_artists'),
    path('all_albums/', views.all_albums, name='all_albums'),



    #path('add_to_playlist/<int:song_id>/', views.add_to_playlist, name='add_to_playlist'),





]
