from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.views import View
from django.views.generic.detail import DetailView
from .models import Post
from django.shortcuts import render
from .forms import PostForm
# from django.http import HttpResponse
# from django.views import View
# from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
    # model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context  

class PostView(DetailView):
    template_name = 'detail.html'
    model = Post

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = Post.objects.create(
            image=form.cleaned_data['image'],
            text=form.cleaned_data['text']
        )
        messages.add_message(self.request, messages.SUCCESS, "Your post was successful")
        
        return super().form_valid(form)



    
