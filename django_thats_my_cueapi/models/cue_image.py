from django.db import models
from .cue import Cue
from .image import Image



class CueImage(models.Model):

    cue = models.ForeignKey(Cue, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)