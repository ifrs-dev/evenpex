from django.db import models
from django.contrib.auth.models import User

CHOICES_EVENT = (
    (1, "Pesquisa"),
    (2, "Ensino"),
    (3, "Extensão"),
)

CHOICES_STATUS = (
    (1, "Inscrit@"),
    (2, "Presente"),
    (3, "Ausente"),
)


class Event(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    start_date = models.DateField()
    kind = models.IntegerField(choices=CHOICES_EVENT, default=1)
    banner = models.ImageField(upload_to='events_banners')

    def __str__(self):
        return self.title


class Registration(models.Model):

    class Meta:
        unique_together = (('event', 'user'),)

    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=CHOICES_STATUS, default=1)

    def __str__(self):
        return self.event.title + ' - ' + self.user.first_name
