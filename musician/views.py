
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm


class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home')

class MusicianDeleteView(DeleteView):
    model = Musician
    template_name = 'musician_delete.html'
    success_url = reverse_lazy('home')


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.musician = Musician.objects.get(user=self.request.user)
        return super().form_valid(form)

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album_delete.html'
    success_url = reverse_lazy('home')

def home(request):
    musician = Musician.objects.all()
    albums = Album.objects.all()
    return render(request, 'home.html', {'musician': musician, 'albums': albums})
