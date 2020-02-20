from django.db import models
from .cue import Cue
from .customer import Customer


class Cue(models.Model):

    notes = models.CharField(max_length=200)
    quoted_price = models.IntegerField()
    builder_contacted = models.BooleanField(null=False)
    time_to_build = models.DateTimeField()
    cue = models.ForeignKey(Cue, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

def __str__(self):
    return self.notes