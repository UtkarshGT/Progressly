from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from dashboard.models import Roadmap


def explore(request):
    roadmaps = Roadmap.objects.all()[:10]
    context = {
        'roadmaps': roadmaps,
    }
    return render(request, 'dashboard/explore.html', context)


def roadmap_detail(request, roadmap_id):
    roadmap = get_object_or_404(Roadmap, pk=roadmap_id)
    context = {
        'roadmap': roadmap
    }
    return render(request, 'dashboard/roadmap_detail.html', context)
