from django.db import models

# Create your models here.
class Data(models.Model):
    encryption_key = models.CharField(max_length = 200)
    encrypted_value = models.CharField(max_length = 500)