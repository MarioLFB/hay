from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=100, label='Name')
    email = models.EmailField(label='Email')
    message = models.TextField(widget=forms.Textarea, label='Message')

    def __str__(self):
        return self.name