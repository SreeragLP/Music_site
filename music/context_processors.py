from music.models import Genre

def menu_links(request):
    mygenre=Genre.objects.all()
    return {'mygenre':mygenre}