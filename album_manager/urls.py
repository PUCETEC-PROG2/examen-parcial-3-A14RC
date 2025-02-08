from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artistas/', views.ArtistaListView.as_view(), name='artista-list'),
    path('artistas/<int:pk>/', views.ArtistaDetailView.as_view(), name='artista-detail'),
    path('artistas/create/', views.ArtistaCreateView.as_view(), name='artista-create'),
    path('artistas/<int:pk>/update/', views.ArtistaUpdateView.as_view(), name='artista-update'),
    path('artistas/<int:pk>/delete/', views.ArtistaDeleteView.as_view(), name='artista-delete'),
    path('albums/', views.AlbumListView.as_view(), name='album-list'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album-detail'),
    path('albums/create/', views.AlbumCreateView.as_view(), name='album-create'),
    path('albums/<int:pk>/update/', views.AlbumUpdateView.as_view(), name='album-update'),
    path('albums/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
    path('artistas/<int:pk>/albums/', views.AlbumByArtistaListView.as_view(), name='album-by-artista-list'),
]