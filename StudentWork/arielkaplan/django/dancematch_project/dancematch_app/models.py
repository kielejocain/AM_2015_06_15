from django.db import models

class Dancer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    date_joined = models.DateField('date joined')
    active_member = models.BooleanField()
    # photo = ImageField() https://docs.djangoproject.com/en/1.8/ref/models/fields/

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Dance(models.Model):
    pass

class Schedule(models.Model):
    pass

class Location(models.Model):
    pass