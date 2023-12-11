from django.shortcuts import render
from django.db.models import Q
from music.models import Genre, Artist, Album, Song

def searchresult(request):
    query = request.GET.get('q')
    results = {'genres': None, 'artists': None, 'albums': None, 'songs': None}

    if query:
        # Search across Genre, Artist, Album, and Song models
        results['genres'] = Genre.objects.filter(g_name__icontains=query)
        results['artists'] = Artist.objects.filter(Artist_name__icontains=query)
        results['albums'] = Album.objects.filter(Album_title__icontains=query)
        results['songs'] = Song.objects.filter(Song_title__icontains=query)


    return render(request, 'search/search.html', {'results': results, 'query': query})



