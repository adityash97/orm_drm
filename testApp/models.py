from django.db import models
import datetime
    
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


#validators
def validate_restaurant_name_begins_with_a(value):
    # breakpoint()
    # if not value.startswith('a') or not value.startswith('A'):
    #     raise ValidationError('Restaurant name must begin with "a"')
    pass
    
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    
class PubDate(models.Model):
    date= models.DateField(default=datetime.date.today)



class Books(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    pub_date = models.ManyToManyField(PubDate,related_name='tracks')

class BookDetails(models.Model):
    book = models.OneToOneField('Books',on_delete=models.CASCADE)
    isbn_no = models.CharField(max_length=255, null=False, blank=False)
    no_of_pages = models.IntegerField()
    language = models.CharField(max_length=100)





    