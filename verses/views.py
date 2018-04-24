from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Verse, Genre, Home, Biography


class Verses(ListView):
    model = Verse
    template_name = 'vers.html'
    paginate_by = 10

    def get_queryset(self):
        self.queryset = Verse.objects.all()
        return self.queryset

    def get_context_data(self, *args, **kwargs):
        news = super().get_context_data(**kwargs)
        news['genre'] = Genre.objects.all()
        return news


class DetailVerse(DetailView):
    model = Verse
    template_name = 'detail_verse.html'

    def get_context_data(self, **kwargs):
        news = super().get_context_data(**kwargs)

        return news


class FilterVerse(ListView):
    model = Verse
    template_name = 'filterverse.html'
    paginate_by = 10

    def get_queryset(self):
        self.queryset = Verse.objects.filter(genre=self.kwargs['pk'])

        return self.queryset

    def get_context_data(self, **kwargs):
        news = super().get_context_data(**kwargs)
        news['genre'] = Genre.objects.all()
        return news


class Home(ListView):
    model = Home
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        news = super().get_context_data(**kwargs)

        return news


class Biography(ListView):
    model = Biography
    template_name = 'biography.html'

    def get_context_data(self, **kwargs):
        news = super().get_context_data(**kwargs)

        return news