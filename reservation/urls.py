from django.urls import include, path

from .models import Comment, Event
from .views import EventListView, EventCreate, EventDelete


app_name = 'reservation'

urlpatterns = [
	path('', EventListView.as_view(), name='event-list'),
	path('<int:week>/', EventListView.as_view(), name='event-list'),
	path('create/', EventCreate.as_view(), name='event-create'),
	path('delete/<pk>/', EventDelete.as_view(), name='event-delete'),
]