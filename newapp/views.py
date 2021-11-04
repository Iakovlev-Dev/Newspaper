#from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from datetime import datetime

from .filters import PostFilter
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.all().order_by('id').reverse()
    paginate_by = 5
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time_now"] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        context['title'] = Post.objects.all()
        context['form'] = PostForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-title']
    paginate_by = 10


    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  
        return context

class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('newapp.add_post',)
    template_name = 'news_create.html'
    form_class = PostForm
    success_url = '/news/'

class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('newapp.change_post',)
    template_name = 'news_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('newapp.delete_post',)
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'prodected_page.html'

    