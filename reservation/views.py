import datetime as dt

from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
# @login_required()
# def index(request):

#     return render(request, "home.html")

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from reservation.models import Event


from django.views.generic.dates import WeekArchiveView

from .forms import EventCreateForm

class EventListView(ListView):
	model = Event

	def get_queryset(self):

		def week_range(week_delta=0):
		    date = dt.date.today()
		    while date.weekday() != 0: # while date is not monday
		        date -= dt.timedelta(1)
		    return date + (dt.timedelta(7) * week_delta), date + dt.timedelta(7) + (dt.timedelta(7) * week_delta)

		print(self.kwargs)
		if 'week' in self.kwargs:
			self.week=self.kwargs['week']
		else:
			self.week=0
		self.start, self.end = week_range(self.week)
		return Event.objects.filter(date__range=[self.start, self.end]).order_by('date', 'start_time')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['WEEKDAYS'] = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		#[('Poniedzialek', 1), ('Wtorek', 2), ('Środa', 3), ('Czwartek', 4), ('Piatek', 5), ('Sobota', 6), ('Niedziela', 0)]
		context['week'] = self.week
		return context


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    success_url = reverse_lazy('reservation:event-list')
    login_url = 'accounts/login/'



    def form_valid(self, form):
    	form.instance.author = self.request.user
    	return super().form_valid(form)



class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('reservation:event-list')

    def dispatch(self, request, *args, **kwargs):
    	event=self.get_object()
    	if not request.user == event.author:
    		raise Exception('PERMISSION ERROR')
    	return super().dispatch(request, *args, **kwargs)

