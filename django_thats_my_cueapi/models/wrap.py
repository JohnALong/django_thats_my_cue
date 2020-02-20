from django.db import models

class Wrap(models.Model):
    name = models.CharField(max_length=50)
    about_wrap = models.CharField(max_length=50)

    def __str__(self):
        return f'A {self.name} has the properties of {self.about_wrap}'