from django.db import models

class Thing(models.Model):
#name: a short string that identifies a thing.
    name = models.CharField()
#description: a slightly longer string that describes a thing.
    description = models.TextField()
#quantity: an integer that identifies the number of items of a thing we possess.
    quantity = models.IntegerField()
