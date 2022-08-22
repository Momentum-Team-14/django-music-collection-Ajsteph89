from django.shortcuts import render

# Create your views here.
def album_list(request):
    return render(request, 'adams_albums/album_list.html', {})