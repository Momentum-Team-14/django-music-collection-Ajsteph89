from django.shortcuts import render, get_object_or_404
from .models import Album
from .forms import AlbumForm
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'adams_albums/album_list.html', {"albums": albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'adams_albums/album_detail.html', {"album": album})

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'adams_albums/album_edit.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'adams_albums/album_edit.html', {'form': form})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')