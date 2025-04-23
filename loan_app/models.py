from django.db import models
from client_list.models import Client

class Loan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField(help_text="Loan term in months")
    interest_rate = models.FloatField()
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan for {self.client.first_name} - {self.amount}"
