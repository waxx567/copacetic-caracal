from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db -> table -> columns
    # id -> primary key (autofield)
    path = models.TextField() # column
    timestamp = models.DateTimeField(auto_now_add=True) # column