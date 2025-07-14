from django.db import models
from django.contrib.auth.models import User
# Create your models here.


Permissions = [
    'export_restaurant',
    'export_rating',
    
]


class Users(User):
    password2 = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = 'Users'
        permissions = [(p,p) for p in Permissions]
        
    def __str__(self):
        return self.name + "__" + self.email + "__" + self.id