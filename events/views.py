from django.views.generic import View, ListView, DetailView
from django.shortcuts import redirect

from events.models import Event, Registration


class EventDetailView(DetailView):
    model = Event
    template_name = 'event-detail.html'


class EventRegistrationView(DetailView):
    model = Event

    def get(self, request, *args, **kwargs):
        return redirect('home')


class EventListView(ListView):
    model = Event
    template_name = 'event-list.html'


class EventSearchListView(EventListView):
    queryset = Event.objects.filter(kind=1)


class EventTeachingListView(EventListView):
    queryset = Event.objects.filter(kind=2)


class EventExtensionListView(EventListView):
    queryset = Event.objects.filter(kind=3)
