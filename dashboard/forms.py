from django.forms import ModelForm

from .models import Entity, Roadmap

class RoadmapForm(ModelForm):
    class Meta:
        model = Roadmap
        fields = ['title', 'description']


class EntityForm(ModelForm):
    class Meta:
        model = Entity
        fields = "__all__"