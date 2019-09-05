# commentaries/urls.py
from django.urls import path
from .views import ThoughtCreateView, ThoughtsListView, list_thoughts, update_thought

app_name = 'commentaries'

urlpatterns = [
    path('list/', ThoughtsListView.as_view(), name='list_thoughts'),
    # path('listall/', list_thoughts, name='listall_thoughts'),
    path('update/<slug:slug>', update_thought, name='update_thought_view'),
    path('add/', ThoughtCreateView.as_view(), name='create_thought'),
]