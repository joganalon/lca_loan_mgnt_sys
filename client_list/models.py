from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    house_num = models.CharField(max_length=50, default='tmp')
    barangay = models.CharField(max_length=100, default='tmp')
    municipality = models.CharField(max_length=100, default='tmp')
    city = models.CharField(max_length=100, default='Naga City')
    province =  models.CharField(max_length=100, default='Camarines Sur')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
