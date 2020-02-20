from django.db import models

class Builder(models.Model):
    name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f'A {self.name} can be contacted at {self.contact_info}'