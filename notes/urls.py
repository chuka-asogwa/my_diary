"""  Defines URL paterns for notes app """
from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page to show all Topics
    path('topics/', views.topics, name='topics'),
    # Page to get a single topic details.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page to Create Topics
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page to create new entry for a topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page to edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]