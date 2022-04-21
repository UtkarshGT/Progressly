from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from dashboard.models import Roadmap


@login_required(login_url="/accounts/google/login")
def index(request):
    if request.user.is_institution:
        roadmaps = request.user.roadmap.all()
    else:
        roadmaps = request.user.follows.all()
    context = {'roadmaps': roadmaps}
    return render(request, 'institution/index.html', context)


@login_required(login_url="/accounts/google/login")
def follow_roadmap(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    roadmap = Roadmap.objects.get(id=q)
    user = request.user
    user.follows.add(roadmap)
    return redirect(reverse('institution'))

@login_required(login_url="/accounts/google/login")
def unfollow_roadmap(request, pk):
    roadmap = Roadmap.objects.get(id=pk)
    user = request.user
    user.follows.remove(roadmap)
    return redirect(reverse('institution'))


@login_required(login_url="/accounts/google/login")
def roadmap_detail(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    context = {
        'roadmap': roadmap
    }
    return render(request, 'institution/roadmap_detail.html', context)