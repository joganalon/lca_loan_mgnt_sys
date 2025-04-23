from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from django.db.models import Q
from django.http import HttpResponse

def client_list(request):
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(
            Q(first_name__icontains=query)
        )
    else:
        clients = Client.objects.all()
        return render(request, 'client_list/list.html',
    {'clients': clients})
