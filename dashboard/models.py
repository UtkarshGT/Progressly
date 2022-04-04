from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models


class Roadmap(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.title
    
class Entity(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    entity_url = models.TextField()

    def __str__(self) -> str:
        return self.title