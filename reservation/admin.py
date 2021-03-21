from django.contrib import admin

from .models import Comment, Event

admin.site.register(Comment)
admin.site.register(Event)