from django.db import models

# models.py
from django.db import models


class Employee( models.Model ):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField( max_length=60 )
    last_name = models.CharField( max_length=60 )
    department = models.CharField( max_length=60 )
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __int__(self):
        return self.id

