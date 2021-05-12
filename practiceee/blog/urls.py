from django.urls import path
from .views import HomePageView, PostView, AddPostView
app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('details/<pk>/', PostView.as_view(), name='detail'),
    path('post/', AddPostView.as_view(), name='post'),

]