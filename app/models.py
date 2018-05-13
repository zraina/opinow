import uuid
from django.db import models
from django.utils import timezone

class Pano(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    p = models.FileField(upload_to='pano')
    location = models.CharField(max_length=200)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Tour(models.Model):
    tour_user = models.ForeignKey('auth.User')
    tour_title = models.CharField(max_length=200)
    tour_location = models.CharField(max_length=200)
    tour_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tour_uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tour_title

class Scene(models.Model):
    scene_title = models.CharField(max_length=200)
    scene_caption = models.CharField(max_length=200)
    scene_url = models.CharField(max_length=200)
    tour = models.IntegerField()

    def __str__(self):
        return self.scene_title
