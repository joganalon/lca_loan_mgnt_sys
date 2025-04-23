from django.db import models

class Client(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_num = models.CharField(max_length=15, default='tmp')
    house_num = models.CharField(max_length=50, default='tmp')
    barangay = models.CharField(max_length=100, default='tmp')
    municipality = models.CharField(max_length=100, default='tmp')
    city = models.CharField(max_length=100, default='Naga City')
    province =  models.CharField(max_length=100, default='Camarines Sur')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.id:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT NEXT VALUE FOR clientID_seq")
                row = cursor.fetchone()
                self.id = row[0]
        super().save(*args, **kwargs)
                
    
