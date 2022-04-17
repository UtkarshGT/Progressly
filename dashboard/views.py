from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import EntityForm, RoadmapForm
from dashboard.models import Entity, Roadmap


def explore(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    roadmaps = Roadmap.objects.filter(title__icontains=q, is_public=True)
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
        print(request.POST)
        Roadmap.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=True if request.POST.get(
                'description') == 'on' else False,
        )

        return redirect('explore')
    context = {'form': form,
               'msg': 'Roadmap'}
    return render(request, 'dashboard/roadmap_form.html', context)


@login_required(login_url="/accounts/google/login")
def roadmap_update(request, pk):
    roadmap = Roadmap.objects.get(id=pk)
    form = RoadmapForm(instance=roadmap)

    if request.method == 'POST':
        form = EntityForm(request.POST)
        if request.user != roadmap.user:
            return HttpResponse("Not valid")
        form = RoadmapForm(request.POST, instance=roadmap)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form,
               'msg': 'Roadmap'}

    return render(request, 'dashboard/roadmap_form.html', context)


@login_required(login_url="/accounts/google/login")
def roadmap_delete(request, pk):
    roadmap = Roadmap.objects.get(id=pk)
    if request.method == 'POST':
        if request.user != roadmap.user:
            return HttpResponse("Not valid")
        roadmap.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/delete.html', {'obj': roadmap})


@login_required(login_url="/accounts/google/login")
def dashboard(request):
    roadmaps = Roadmap.objects.filter(user=request.user)
    context = {'roadmaps': roadmaps}
    return render(request, 'dashboard/dashboard.html', context)


# Create
@login_required(login_url="/accounts/google/login")
def entity_form(request, pk):
    form = EntityForm()
    if request.method == 'POST':
        roadmap = Roadmap.objects.get(id=pk)
        if request.user != roadmap.user:
            return HttpResponse("Not valid")
        Entity.objects.create(
            roadmap=roadmap,
            title=request.POST.get('title'),
            entity_url=request.POST.get('entity_url')
        )
        return redirect('explore')
    context = {'form': form,
               'msg': 'Source'}
    return render(request, 'dashboard/roadmap_form.html', context)


@login_required(login_url="/accounts/google/login")
def entity_update(request, pk):
    entity = Entity.objects.get(id=pk)
    form = EntityForm(instance=entity)

    if request.method == 'POST':
        if request.user != entity.roadmap.user:
            return HttpResponse("Not valid")

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
        if request.user != entity.roadmap.user:
            return HttpResponse("Not valid")
        entity.delete()
        return redirect(reverse('roadmap', args=[entity.roadmap.id]))
    return render(request, 'dashboard/delete.html', {'obj': entity})


@login_required(login_url="/accounts/google/login")
def toggle_entity(request, pk):
    entity = Entity.objects.get(id=pk)
    entity.is_completed = not entity.is_completed
    entity.save()
    return redirect(reverse('roadmap', args=[entity.roadmap.id]))


@login_required(login_url="/accounts/google/login")
def import_roadmap(request, pk):
    roadmap = Roadmap.objects.get(id=pk)
    new_roadmap = Roadmap.objects.create(
        user=request.user,
        title=roadmap.title,
        description=roadmap.description,
        is_public=False
    )
    for entity in roadmap.entity_set.all():
        Entity.objects.create(
            roadmap=new_roadmap,
            title=entity.title,
            entity_url=entity.entity_url,
            is_completed=False,
        )
    return redirect('dashboard')
