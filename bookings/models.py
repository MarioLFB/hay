from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Table(models.Model):
    '''
    Model for the Table, used for booking a table
    '''
    table_name = models.CharField(max_length=100)
    table_phone = models.CharField(max_length=100, default='+44 20 7123 4567')
    table_email = models.EmailField(default='email@email.com')
    table_capacity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )

    table_date = models.DateField(default=date.today)
    table_time = models.TimeField(default='08:00:00')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.table_name
