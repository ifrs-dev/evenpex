from django.db import models

CHOICES_EVENT = (
    (1, "Pesquisa"),
    (2, "Ensino"),
    (3, "Extensão"),
)

class Event(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    start_date = models.DateField()
    kind = models.IntegerField(choices=CHOICES_EVENT)
