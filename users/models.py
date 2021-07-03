from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user_types = (
        ('Admin', 'Admin'),
        ('Operator','Operator'),
        ('Customer', 'Customer'),
    )

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    user_type = models.CharField(max_length = 20, choices=user_types, default = 'Customer')
    
    def __str__(self):
        return f'{self.user.username} Profile'