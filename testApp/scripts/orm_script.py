from django.contrib.auth.models import User
from testApp.models import Restaurant, Rating, Sale,Author,Books,PubDate,Sale
from django.utils import timezone
from django.db import connection
from django.db import models
from django.db.models import functions
from pprint import pprint
from django.db.models import F,Q,Value
from django.db.models.functions import Concat
from django.db.models.fields import CharField
from datetime import time
from django.db.models.functions import Coalesce
from django.db.models import Value,Case,When,Subquery,OuterRef
from django.db import transaction
def run():
    # enter code below - Transaction Practice
    # with transaction.atomic():
    #     try:
    #         author = Author.objects.get(id=1)
    #         author.name = 'Aditya 2'
    #         author.save()
    #         raise ValueError("OOps! Some value error")
    #     except Exception as e:
    #         transaction.set_rollback(True)
    #         print("Error : ",e)
    # try:
    #     with transaction.atomic():
    #         author = Author.objects.get(id=1)
    #         author.name = 'Aditya 2'
    #         author.save()
    #         raise ValueError("OOps! Some value error")
    # except Exception as e:
    #         # transaction.set_rollback(True)
    #         print("Error : ",e)
    
            
    
    
    
    
    print("*"*30)
    print("-"*30)
    pprint(connection.queries)
    print("-"*30)
    