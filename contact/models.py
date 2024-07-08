from django.db import models
from django.core.validators import EmailValidator
from validate_email import validate_email
from django.core.exceptions import ValidationError

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if not validate_email(self.email):
            raise ValidationError({'email': 'Invalid email format'})



    def __str__(self):
        return self.name