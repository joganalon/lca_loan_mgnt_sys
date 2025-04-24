from django import forms
from .models import Client, Loan, Disbursement
import datetime

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class LoanForm(forms.ModelForm):
    application_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    start_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    interest = forms.DecimalField(
        initial=15.0,
        label="Interest (%)",
        widget=forms.NumberInput(attrs={'step':'0.01', 'id': 'id_interest'})
    )

    class Meta:
        model = Loan
        fields = ['amount', 'interest']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'id': 'id_amount',
                'step': '0.01',
                'class': 'form-control'
            })
        }


class DisbursementForm(forms.ModelForm):
    class Meta:
        model = Disbursement
        fields = ['amount', 'disbursement_date']
        widgets = {
            'disbursement_date': forms.DateInput(attrs={'type':
    'date'}),
            'amount': forms.NumberInput(attrs={
                'id': 'id_disbursement_amount',
                'readonly': 'readonly',
                'class': 'form-control',
                'step': '0.01'
            }),
        }
