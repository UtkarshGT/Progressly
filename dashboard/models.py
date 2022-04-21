from django.db import models
from users.models import CustomUser as User

class Roadmap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roadmap', null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
class Entity(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    entity_url = models.URLField(max_length=300)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title