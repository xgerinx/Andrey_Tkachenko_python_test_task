from django.views.generic import ListView, DetailView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 10


class PostView(DetailView):
    model = Post
    template_name = 'post.html'
