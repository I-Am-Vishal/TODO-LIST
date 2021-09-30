from django.db import models
from django.contrib.auth.models import User
# import uuid

# Create your models here.

class Task(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    description =models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    # id = models.UUIDField(default=uuid.uuid4,unique = True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

# unique = True <-- use this attribute when we want make the field as unique