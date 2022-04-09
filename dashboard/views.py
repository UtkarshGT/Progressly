from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import EntityForm, RoadmapForm
from dashboard.models import Entity, Roadmap


def explore(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    roadmaps = Roadmap.objects.filter(title__icontains=q)
    context = {
        'roadmaps': roadmaps,
    }
    return render(request, 'dashboard/explore.html', context)


def roadmap_detail(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    context = {
        'roadmap': roadmap
    }
    return render(request, 'dashboard/roadmap_detail.html', context)

# Create


@login_required(login_url="/accounts/google/login")
def roadmap_form(request):
    form = RoadmapForm()
    if request.method == 'POST':
        form = RoadmapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('explore')
    context = {'form': form,
               'msg': 'Roadmap'}
    return render(request, 'dashboard/roadmap_form.html', context)


@login_required(login_url="/accounts/google/login")
def roadmap_update(request, pk):
    roadmap = Roadmap.objects.get(id=pk)
    form = RoadmapForm(instance=roadmap)

    if request.method == 'POST':
        form = RoadmapForm(request.POST, instance=roadmap)
        if form.is_valid():
            form.save()
            return redirect('explore')

    context = {'form': form,
               'msg': 'Roadmap'}

    return render(request, 'dashboard/roadmap_form.html', context)


@login_required(login_url="/accounts/google/login")
def roadmap_delete(request, pk):
    roadmap = Roadmap.objects.get(id=pk)
    if request.method == 'POST':
        roadmap.delete()
        return redirect('explore')
    return render(request, 'dashboard/delete.html', {'obj': roadmap})


# Create
@login_required(login_url="/accounts/google/login")
def entity_form(request):
    form = EntityForm()
    if request.method == 'POST':
        form = EntityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('explore')
    context = {'form': form,
               'msg': 'Source'}
    return render(request, 'dashboard/roadmap_form.html', context)


@login_required(login_url="/accounts/google/login")
def entity_update(request, pk):
    entity = Entity.objects.get(id=pk)
    form = EntityForm(instance=entity)

    if request.method == 'POST':
        form = EntityForm(request.POST, instance=entity)
        if form.is_valid():
            form.save()
            return redirect('explore')
    context = {'form': form,
               'msg': 'Source'}
    return render(request, 'dashboard/roadmap_form.html', context)


@login_required(login_url="/accounts/google/login")
def entity_delete(request, pk):
    entity = Entity.objects.get(id=pk)
    if request.method == 'POST':
        entity.delete()
        return redirect('explore')
    return render(request, 'dashboard/delete.html', {'obj': entity})
