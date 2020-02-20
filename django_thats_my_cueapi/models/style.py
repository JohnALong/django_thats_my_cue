from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=50)
    about_style = models.CharField(max_length=50)

    def __str__(self):
        return f'A {self.name} has the properties of {self.about_style}'