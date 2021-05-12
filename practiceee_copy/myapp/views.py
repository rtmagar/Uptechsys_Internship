from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Post


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
    # model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostView(DetailView):
    template_name = 'detail.html'
    model = Post
    



    

    
