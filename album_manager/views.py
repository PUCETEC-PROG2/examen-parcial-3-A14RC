from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Artista, Album

def home(request):
    return render(request, 'home.html')

class ArtistaListView(ListView):
    model = Artista
    template_name = 'artista_list.html'

class ArtistaDetailView(DetailView):
    model = Artista
    template_name = 'artista_detail.html'

class ArtistaCreateView(CreateView):
    model = Artista
    template_name = 'artista_form.html'
    fields = ['nombre', 'descripcion']

    def get_success_url(self):
        return reverse_lazy('artista-list')

class ArtistaUpdateView(UpdateView):
    model = Artista
    template_name = 'artista_form.html'
    fields = ['nombre', 'descripcion']

class ArtistaDeleteView(DeleteView):
    model = Artista
    template_name = 'artista_confirm_delete.html'
    success_url = reverse_lazy('artista-list')

class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album_detail.html'

class AlbumCreateView(CreateView):
    model = Album
    template_name = 'album_form.html'
    fields = ['titulo', 'anio_lanzamiento', 'genero', 'artista', 'portada']

    def get_success_url(self):
        return reverse_lazy('album-list')

class AlbumUpdateView(UpdateView):
    model = Album
    template_name = 'album_form.html'
    fields = ['titulo', 'anio_lanzamiento', 'genero', 'artista', 'portada']

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'
    success_url = reverse_lazy('album-list')

class AlbumByArtistaListView(ListView):
    model = Album
    template_name = 'album_by_artista_list.html'

    def get_queryset(self):
        self.artista = get_object_or_404(Artista, pk=self.kwargs['pk'])
        return Album.objects.filter(artista=self.artista)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artista'] = self.artista
        return context