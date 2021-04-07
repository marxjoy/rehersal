from django.contrib.auth.models import User

from django.db import models

from datetime import date

class Event(models.Model):
	title = models.CharField(max_length=16, default='Próba')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	date = models.DateField(default=date.today)
	start_time = models.TimeField(default='11:00')
	end_time = models.TimeField(default='21:30')
	description = models.CharField(max_length=128, blank=True, null=True)
	is_periodic = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.title} ({self.date}) of {self.author}"


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE) 
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments') 
	content = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.author} commented {self.event} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"