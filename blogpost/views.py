from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from blogpost.models import Blogpost


class BlogpostCreateView(CreateView):
    model = Blogpost
    fields = ('title', 'body',)
    success_url = reverse_lazy('blogpost:list')


class BlogpostUpdateView(UpdateView):
    model = Blogpost
    fields = ('title', 'body',)
    success_url = reverse_lazy('blogpost:list')


class BlogpostListView(ListView):
    model = Blogpost


class BlogpostDetailView(DetailView):
    model = Blogpost


class BlogpostDeleteView(DeleteView):
    model = Blogpost
    success_url = reverse_lazy("blogpost:list")