from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=1000)
    
    def __str__(self):#to make the retrieving data as a string and not as a queryset.
        return self.title
 
  