from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    g_name = models.CharField(max_length=50)
    g_photo = models.ImageField(upload_to='media/genre_photos/', null=True, blank=True)
    g_description = models.TextField()

    def __str__(self):
        return self. g_name

class Artist(models.Model):
    Artist_name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    Artist_photo = models.ImageField(upload_to='media/artist_photos/', null=True, blank=True)
    Artist_description = models.TextField()

    def __str__(self):
        return self.Artist_name

class Album(models.Model):
    Album_title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Album_price = models.DecimalField(max_digits=10, decimal_places=2)
    Album_photo = models.ImageField(upload_to='media/album_photos/', null=True, blank=True)
    Album_description = models.TextField()

    def __str__(self):
        return self.Album_title

class Song(models.Model):
    Song_title = models.CharField(max_length=100, default='Untitled')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=1)
    file = models.FileField(upload_to='media/songs/', null=True, blank=True)

    def __str__(self):
        return self.Song_title



class Playlist(models.Model):
    song=models.ForeignKey(Song,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)
    date_added=models.DateField(auto_now_add=True)

