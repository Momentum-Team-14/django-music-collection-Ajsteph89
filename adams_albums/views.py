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
            album.author = request.user
            album.created_at = timezone.now()
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'adams_albums/album_edit.html', {'form': form})

def album_edit(request, pk):
    post = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=post)
        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.created_at = timezone.now()
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=post)
    return render(request, 'adams_albums/album_edit.html', {'form': form})
