from django.db import models
from django_quill.fields import QuillField


# Performers
class Performer(models.Model):
    name = models.CharField(max_length=100)
    bio = QuillField(blank=True, default="Biography forthcoming...")
    website = models.URLField(max_length=1000, blank=True)
    facebook = models.URLField(max_length=1000, blank=True)
    twitter = models.URLField(max_length=1000, blank=True)
    instagram = models.URLField(max_length=1000, blank=True)
    imdb = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# Plays
class Play(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    audioFile = models.FileField(upload_to='audio/')
    image = models.ImageField(upload_to='images/', default='static/assets/artwork/thereordering_cassietaggart.jpg')
    external_Link = models.URLField(max_length=1000)
    performers = models.ManyToManyField(Performer, related_name='plays')
    date_Added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_Added']


# Creators
class Creator(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='Creator')
    bio = QuillField()
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name