"""  Defines URL paterns for notes app """
from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
]