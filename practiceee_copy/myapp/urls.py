from django.urls import path, include
from .views import HomePageView, PostView

app_name = 'myapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('details/<pk>', PostView.as_view(), name='detail')
]