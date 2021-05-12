from django.urls import path, include
urlpatterns = [
    path('', FormView().as_view, name= 'form')
]