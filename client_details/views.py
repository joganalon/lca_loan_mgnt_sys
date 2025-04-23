from django.shortcuts import render, get_object_or_404
from client_list.models import Client

def client_profile(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client_details/profile.html', {'client': client})


