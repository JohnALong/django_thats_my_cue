from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=50)
    route = models.CharField(max_length=50)

    def __str__(self):
        return self.name
