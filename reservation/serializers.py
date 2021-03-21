# from rest_framework import routers, serializers, viewsets

# from .models import Comment, Event

# # Serializers define the API representation.
# class CommentSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['author', 'event', 'content', 'created_at']


# class EventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Event
#         fields = ['id', 'author', 'date', 'start_time', 'created_at', 'end_time' ,'description', 'title', 'comments']