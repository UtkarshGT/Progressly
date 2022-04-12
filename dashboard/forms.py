from django.forms import ModelForm

from .models import Entity, Roadmap

class RoadmapForm(ModelForm):
    class Meta:
        model = Roadmap
        fields = ['title', 'description', 'is_public']


class EntityForm(ModelForm):
    class Meta:
        model = Entity
        fields = ['title','entity_url']