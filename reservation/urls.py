from django.urls import include, path
from django.contrib.auth import views as auth_views
#from rest_framework import routers, serializers, viewsets

from . import views

from .models import Comment, Event
#from .serializers import CommentSerializer, EventSerializer

from .views import EventListView, EventCreate, EventDelete

# # ViewSets define the view behavior.
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# class EventViewSet(viewsets.ModelViewSet):
# 	queryset = Event.objects.all()
# 	serializer_class = EventSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'comments', CommentViewSet)
# router.register(r'events', EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'reservation'

urlpatterns = [
	#path('', views.index, name='index'),
	path('', EventListView.as_view(), name='event-list'),
	path('<int:week>/', EventListView.as_view(), name='event-list'),
	path('create/', EventCreate.as_view(), name='event-create'),
	path('delete/<pk>/', EventDelete.as_view(), name='event-delete'),
	#path('accounts/', include('django.contrib.auth.urls')),
      #  path('', include(router.urls))
]