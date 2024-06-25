from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Table(models.Model):
    table_name = models.CharField(max_length=100)
    table_capacity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    table_data = models.DateField()

    def __str__(self):
        return self.table_name
