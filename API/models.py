from django.db import models

# Create your models here.

class APIModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    area = models.DecimalField(decimal_places=0 ,max_digits=5)
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return '{} | {} | {} | {}'.format(self.name, self.address, self.area, self.email)
        