from django.views.generic import View, ListView, DetailView
from django.shortcuts import redirect

from events.models import Event, Registration


class MyRegistrationsListView(ListView):
    model = Registration
    template_name = 'my-events.html'

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)


class EventDetailView(DetailView):
    model = Event
    template_name = 'event-detail.html'


class EventRegistrationView(DetailView):
    model = Event

    def get(self, request, *args, **kwargs):
        Registration.objects.create(event=self.get_object(), user=request.user)
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
