from myapp.forms import PostForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Post
from django.contrib import messages


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

class NewPostView(FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        new_object = Post.objects.create(
            title=form.cleaned_data['title'],
            image=form.cleaned_data['image']
            
        )    
        messages.add_message(self.request, messages.SUCCESS, "Your Post was successfull")                           
        return super().form_valid(form)
    
    

    



    

    
