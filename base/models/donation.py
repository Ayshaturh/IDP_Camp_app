from django.db import models
from .user import User

# Create your models here.
class Donation(models.Model):

    DONATION_TYPES = [
        ('money', 'Money'),
        ('hospital', 'Hospital Facilities'),
        ('food', 'Food'),
        ('shelter', 'Shelter'),
        ('clothing', 'Clothing'),
    ]
    
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPES ) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)   
    reference = models.CharField(max_length=128,null=True, blank=True)
    description = models.TextField(null=True, blank=True)  # For other types of donations
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
       return f"{self.get_donation_type_display()} - {self.amount if self.donation_type == 'money' else self.description}"
    

   
    
