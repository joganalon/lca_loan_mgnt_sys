from django.db import models
from django.utils import timezone

class Client(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_num = models.CharField(max_length=15)
    house_num = models.CharField(max_length=50)
    barangay = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='Naga City')
    province =  models.CharField(max_length=100, default='Camarines Sur')
    occupation =  models.CharField(max_length=100, default='business')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    #added this because I used sequence in mysql
    #to apply what was discussed during classes
    
    def save(self, *args, **kwargs):
        if not self.id:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT NEXT VALUE FOR clientID_seq")
                row = cursor.fetchone()
                self.id = row[0]
        super().save(*args, **kwargs)

class Loan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField(default=0.15)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()

    def __str__(self):
        return f"Loan for {self.client.first_name} - {self.amount}"


class Disbursement(models.Model):
    loan = models.ForeignKey('Loan', on_delete=models.CASCADE, related_name='disbursements')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    disbursement_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Disbursed ₱{self.amount} on {self.date} for Loan #{self.loan.id}"


class Payment(models.Model):
    loan = models.ForeignKey('Loan', on_delete=models.CASCADE, related_name='payments')
    starting_date = models.DateField(auto_now_add=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    collector = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment of ₱{self.amount} on {self.date} for Loan #{self.loan.id}"
    

    
    
