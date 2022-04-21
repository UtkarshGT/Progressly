from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/google/login")
def index(request):
    context = {}
    return render(request, 'institution/index.html', context)
