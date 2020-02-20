from django.db import models
from .builder import Builder
from .wrap import Wrap
from .style import Style
from .image import Image

class Cue(models.Model):

    about_cue = models.CharField(max_length=200)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    wrap = models.ForeignKey(Wrap, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

def __str__(self):
    return self.about_cue
    