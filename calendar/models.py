from django.db import models
from enum import Enum
from contract.models import property

# Fixed choices/static
# Fixed calendar type choices
#class calendarType(Enum):



class calendar(models.Model):
    property = models.ForeignKey(property, on_delete = models.CASCADE)
    date = models.DateTimeField()
    #type = models.CharField(choices = [(code, code.value) for code in calendarType])
