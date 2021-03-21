from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Event

import datetime as dt


class EventCreateForm(ModelForm):
	class Meta:
		model = Event
		fields = ['title', 'date', 'start_time', 'end_time',  'description']

	def clean(self):
		cleaned_data = super().clean()
		end_time = cleaned_data.get("end_time")
		start_time = cleaned_data.get("start_time")
		date = cleaned_data.get("date")

		if all((date, start_time, end_time)): # Validate only if datetime fields are correct

			if end_time.hour == 21 and end_time.minute > 30:
				msg = "21:30 to max"
				self.add_error('end_time', msg)
			if end_time.hour >= 22 :
				msg = "21:30 to max"
				self.add_error('end_time', msg)
			if start_time.hour <= 10 :
				msg = "11:00 to min"
				self.add_error('start_time', msg)

			if start_time >= end_time:
				msg = "Start time nie może być większy niż End time"
				self.add_error('start_time', msg)


			
			print(date)
			same_day_events = Event.objects.filter(date=date).filter(start_time__gte=start_time).filter(end_time__lte=end_time)
			print(same_day_events)
			if same_day_events:
				msg = "Jest już zajęte"
				self.add_error('date', msg)




