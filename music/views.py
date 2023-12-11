from django.shortcuts import render,redirect
from music.models import Genre,Artist,Album,Song,Playlist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import random
from mysub.models import Account,Subscribe
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.

def home(request):
    genres = Genre.objects.all()
    albums = Album.objects.all()
    artists = Artist.objects.all()
    songs = Song.objects.all()

    shuffled_artists = list(artists)
    shuffled_songs = list(songs)
    shuffled_trends = list(albums)


    random.shuffle(shuffled_artists)
    random.shuffle(shuffled_songs)
    random.shuffle(shuffled_trends)

    return render(request, 'music/home.html', {'genres': genres,
                                               'artists': shuffled_artists[:3],
                                               'songs': shuffled_songs[:1],
                                               'trends': shuffled_trends[:3]})


@login_required
def artist(request, a):
    # Filter artists based on the genre name
    b = Artist.objects.filter(genre__g_name=a)

    # Retrieve the genre object
    genre = Genre.objects.get(g_name=a)
    return render(request, 'music/artist.html', {'b': b, 'genre': genre})


@login_required
def albums(request, a):

    # Filter albums based on the artist name
    al = Album.objects.filter(artist__Artist_name=a)

    # Retrieve the artist object
    artist = Artist.objects.get(Artist_name=a)

    return render(request, 'music/albums.html', {'albums': al, 'artist': artist})





@login_required
def songs(request, a):

    # Filter songs based on the album title
    songs = Song.objects.filter(album__Album_title=a)

    album = Album.objects.get(Album_title=a)

    return render(request, 'music/songs.html', {'songs': songs, 'album': album})




# #this is for playing songs
# def play(request,a):
#     song=Song.objects.get(pk=a)
#     return render(request, 'music/play.html', {'song': song})



@login_required
def play(request, a):
    user = request.user

    try:
        s = Subscribe.objects.get(user=user)
    except ObjectDoesNotExist:
        # Redirect the user to the subscribe page when Subscribe object does not exist
        return redirect('mysub:sub')

    if s :
        song = Song.objects.get( pk=a)

        # Get the album and all songs in that album
        album = song.album
        all_songs = list(album.song_set.all())  # Convert  to a list

        # Find the index of the current song in the list of all songs
        current_song_index = all_songs.index(song)

        # Calculate the index of the previous and next songs
        previous_song_index = (current_song_index - 1) % len(all_songs)
        next_song_index = (current_song_index + 1) % len(all_songs)

        # Get the previous and next songs
        previous_song = all_songs[previous_song_index]
        next_song = all_songs[next_song_index]

        return render(request, 'music/play.html', {
            'song': song,
            'previous_song': previous_song,
            'next_song': next_song,
        })











def playlist(request):
    if request.user.is_authenticated:
        # Retrieve the user's playlist entries
        user_playlist = Playlist.objects.filter(user=request.user)
        return render(request, 'music/playlist.html', {'playlist': user_playlist})
    else:
        # when the user is not authenticated
        return redirect('music:login')



def add_to_playlist(request, a):

    song = Song.objects.get(pk=a)

    # Check if the song is already in the user's playlist
    if Playlist.objects.filter(user=request.user, song=song).exists():
        pass
    else:
        # Add the song to the playlist
        Playlist.objects.create(user=request.user, song=song)

    return playlist(request)    #changed as favts




def playlist_remove(request, p):

    playlist_entry = Playlist.objects.get (pk=p)

    # Check if the user making the request is the owner of the playlist entry
    if request.user == playlist_entry.user:
        # Delete the playlist entry
        playlist_entry.delete()

    else:
       pass
    return redirect('music:playlist')



# def all_artists(request):
#     # Get all artists ordered alphabetically
#     artists = Artist.objects.all().order_by('Artist_name')
#     return render(request, 'music/all_artists.html', {'artists': artists})



def all_artists(request):

    # Get all artists ordered alphabetically
    artists = Artist.objects.all().order_by('Artist_name')

    # Create a dictionary to group artists by the first letter of their name
    grouped_artists = {}
    for artist in artists:
        first_letter = artist.Artist_name[0].upper()
        if first_letter not in grouped_artists:
            grouped_artists[first_letter] = []
        grouped_artists[first_letter].append(artist)

    return render(request, 'music/all_artists.html', {'grouped_artists': grouped_artists})




def all_albums(request):

    # Get all albums ordered alphabetically
    albums = Album.objects.all().order_by('Album_title')

    # Create a dictionary to group albums by the first letter of their name
    grouped_albums = {}

    for album in albums:
        first_letter = album.Album_title[0].upper()
        if first_letter not in grouped_albums:
            grouped_albums[first_letter] = []

        grouped_albums[first_letter].append(album)

    return render(request, 'music/all_albums.html', {'grouped_albums': grouped_albums})





def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        p1 = request.POST['p1']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(p==p1):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return redirect('music:home')

    return render(request,'music/register.html')


def user_login(request):
    if (request.method == "POST"):
        u = (request.POST['u'])
        p = (request.POST['p'])
        user = authenticate(username=u, password=p)

        if user:
            login(request,user)
            return redirect('music:home')
        else:
            messages.error(request, "invalid credentails")
    return render(request,'music/login.html')


def user_logout(request):
    logout(request)
    return user_login(request)


def shuffle(request):
    songs = Song.objects.all()
    shuffled_songs = list(songs)
    random.shuffle(shuffled_songs)
    return render(request,'music/shuffle.html',{'songs':shuffled_songs[:1]})