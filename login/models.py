from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    fiscal_ID = models.CharField(max_length = 20)

    def __str__(self):
        return self.user.username        # Returns the specific value as the value of the assigned_name
