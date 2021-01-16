from django.db import models
import datetime

# Create your models here.

# Actors
class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to='images/', default='static/assets/icons/user-solid.svg')
    website = models.URLField(max_length=1000, blank=True)
    facebook = models.URLField(max_length=1000, blank=True)
    twitter = models.URLField(max_length=1000, blank=True)
    instagram = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

# Episodes
class Episode(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    audioFile = models.FileField(upload_to='audio/')
    image = models.ImageField(upload_to='images/', default='static/assets/artwork/thereordering_cassietaggart.jpg')
    external_Link = models.URLField(max_length=1000)
    actors = models.ManyToManyField(Actor)
    date_Added = datetime.datetime.now()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_Added']