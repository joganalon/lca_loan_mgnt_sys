from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Loan, Disbursement
from .forms import ClientForm, LoanForm, DisbursementForm
from django.db.models import Q
from django.http import HttpResponse

def client_list(request):
    query = request.GET.get('q', '')
    if query:
        clients = Client.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
    else:
        clients = Client.objects.all()
        
    return render(request, 'client_list/list.html',
    {'clients': clients})


def client_create(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        loan_form = LoanForm(request.POST)
        disbursement_form = DisbursementForm(request.POST)
        
        if client_form.is_valid() and loan_form.is_valid() and disbursement_form.is_valid():
            client = client_form.save()
            
            loan = loan_form.save(commit=False)
            loan.client = client
            loan.save()
            
            disbursement = disbursement_form.save(commit=False)
            disbursement.loan = loan
            disbursement.save()

            start_date = loan.start_date
            current_day = start_date
            payments = []

            while len(payments) < 40:
                if current_day.weekday() != 6:
                    payments.append(Payment(loan=loan, due_date=current_day))
                current_day += timedelta(days=1)

            Payment.objects.bulk_create(payments)
                    
            
            return redirect('client_list')
    else:
        client_form = ClientForm()
        loan_form = LoanForm()
        disbursement_form = DisbursementForm()

    return render(request, 'client_list/form.html', {
        'client_form': client_form,
        'loan_form': loan_form,
        'disbursement_form': disbursement_form
    })

