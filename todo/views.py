from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BookModel
from django.urls import reverse_lazy

# Create your views here.

class BookList(ListView):
    template_name = 'list.html'
    model = BookModel


class BookDetail(DetailView):
    template_name = 'detail.html'
    model = BookModel


class BookCreate(CreateView):
    template_name = 'create.html'
    model = BookModel
    fields = ('title', 'price', 'memo')
    success_url = reverse_lazy('list')


class BookDelete(DeleteView):
    template_name = 'delete.html'
    model = BookModel
    success_url = reverse_lazy('list')


class BookUpdate(UpdateView):
    template_name = 'update.html'
    model = BookModel
    fields = ('title', 'price', 'memo')
    success_url = reverse_lazy('list')