from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('albums/<int:pk>', views.album_detail, name='album_detail'),
    path('album/new/', views.album_new, name='album_new'),
    path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('delete_album/<int:pk>', views.delete_album, name='delete_album')
]