from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Businesses(models.Model):
    owner = models.ForeignKey(User, related_name="business_owner", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True, default=None)
    employee_size = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
