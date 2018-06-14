from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect
from django.views.generic import View, ListView, DetailView

from events.models import Event, Registration


class MyRegistrationsListView(ListView):
    model = Registration
    template_name = 'my-events.html'

    def get_queryset(self):
        objects = Registration.objects.filter(user=self.request.user)
        return objects.order_by('event__start_date')


class EventDetailView(DetailView):
    model = Event
    template_name = 'event-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        try:
            events = Registration.objects.filter(event=self.get_object(), user=user)
            if events.exists():
                context['registred'] = True
            else:
                context['registred'] = False
        except:
            context['not_user'] = True
        return context

class EventRegistrationView(DetailView):
    model = Event

    def get(self, request, *args, **kwargs):
        Registration.objects.create(event=self.get_object(), user=request.user)
        return redirect('my-events')


class EventListView(ListView):
    model = Event
    template_name = 'event-list.html'


class EventSearchListView(EventListView):
    queryset = Event.objects.filter(kind=1)


class EventTeachingListView(EventListView):
    queryset = Event.objects.filter(kind=2)


class EventExtensionListView(EventListView):
    queryset = Event.objects.filter(kind=3)
