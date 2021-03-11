from django.db import models
from django_quill.fields import QuillField
from datetime import datetime
from cloudinary.models import CloudinaryField


# Performers
class Performer(models.Model):
    name = models.CharField(max_length=100)
    bio = QuillField(blank=True)
    imdb = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# Plays
class Play(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    audioFile = CloudinaryField('audio', overwrite=True, resource_type='video')
    image = CloudinaryField('image', overwrite=True, resource_type='image', default='sweetnectar_cassietaggart_default_qz039o.jpg')
    apple_Link = models.CharField(max_length=1000, default='#')
    google_Link = models.CharField(max_length=1000, default='#')
    amazon_Link = models.CharField(max_length=1000, default='#')
    stitcher_Link = models.CharField(max_length=1000, default='#')
    performers = models.ManyToManyField(Performer, related_name='plays')
    release_Date = models.DateTimeField(editable=True, default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-release_Date']


# Creators
class Creator(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='Creator')
    bio = QuillField()
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']