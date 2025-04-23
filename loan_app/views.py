from django.shortcuts import render, get_object_or_404
from client_list.models import Client
from .forms import LoanApplicationForm

def loan_application_create(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    form = LoanApplicationForm(request.POST or None,
    initial={'client': client })

    if request.method == 'POST' and form.is_valid():
        loan = form.save(commit=False)
        loan.client = client
        loan.save()
        return redirect('loan_detail', pk=loan.pk)

    return render(request, 'loan_app/loan_form.html', {'form': form,
    'client': client})


