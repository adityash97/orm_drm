from django.contrib import admin
from .models import Books,Author,PubDate
# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(PubDate)