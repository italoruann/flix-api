from django.db import models

from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies') # um-para-muitos 1-N
    release_date = models.DateField(blank=True, null=True)
    actors = models.ManyToManyField(Actor, related_name='movies') # muitos-para-muitos N-N
    synopsis = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title