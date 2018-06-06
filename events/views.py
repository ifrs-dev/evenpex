from django.views.generic import ListView, DetailView

from events.models import Event


class EventDetailView(DetailView):
    model = Event
    template_name = 'event-detail.html'


class EventListView(ListView):
    model = Event
    template_name = 'event-list.html'


class EventSearchListView(EventListView):
    queryset = Event.objects.filter(kind=1)


class EventTeachingListView(EventListView):
    queryset = Event.objects.filter(kind=2)


class EventExtensionListView(EventListView):
    queryset = Event.objects.filter(kind=3)
