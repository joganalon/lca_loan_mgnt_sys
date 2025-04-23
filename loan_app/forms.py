from django import forms
from .models import Loan

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['amount', 'term', 'interest_rate']
        widgets = {
            'amount': forms.NumberInput(attrs={'class':
    'form-control'}),
            'term': forms.NumberInput(attrs={'class':
    'form-control'}),
            'interest_rate': forms.NumberInput(attrs={'class':
    'form-control'}),

        }
