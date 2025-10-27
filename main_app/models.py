from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django_quill.fields import QuillField
from cloudinary.models import CloudinaryField

def validate_future_date(value):
    if value > timezone.now():
        raise ValidationError('Release date cannot be in the future.')


# Performers
class Performer(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    bio = QuillField(blank=True)
    imdb = models.URLField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if not self.name:
            raise ValidationError('Performer must have a name')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Performer'
        verbose_name_plural = 'Performers'
        indexes = [
            models.Index(fields=['name']),
        ]


# Plays
class Play(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    description = QuillField(blank=True)
    audioFile = CloudinaryField('audio', overwrite=True, resource_type='video', null=False)
    image = CloudinaryField('image', overwrite=True, resource_type='image',
                          default='sweetnectar_cassietaggart_default_qz039o.jpg', null=False)
    performers = models.ManyToManyField(Performer, related_name='plays')
    release_Date = models.DateTimeField(
        editable=True,
        default=timezone.now,
        db_index=True,
        validators=[validate_future_date]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if not self.name:
            raise ValidationError('Play must have a name')
        if not self.audioFile:
            raise ValidationError('Play must have an audio file')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-release_Date']
        verbose_name = 'Play'
        verbose_name_plural = 'Plays'
        indexes = [
            models.Index(fields=['-release_Date']),
            models.Index(fields=['name']),
        ]


# Creators
class Creator(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    title = models.CharField(max_length=100, default='Creator')
    bio = QuillField()
    email = models.EmailField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if not self.name:
            raise ValidationError('Creator must have a name')
        if not self.bio:
            raise ValidationError('Creator must have a bio')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Creator'
        verbose_name_plural = 'Creators'
        indexes = [
            models.Index(fields=['name']),
        ]
