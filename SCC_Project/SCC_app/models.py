from django.db import models




            
class Guest(models.Model):
    provider_name = models.CharField(max_length = 100)
    client = models.CharField(max_length=100)
    signed_out_by = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length =30)
    username = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
