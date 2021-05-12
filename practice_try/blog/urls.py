from .views import HomePageView
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name = 'index')
]