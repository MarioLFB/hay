from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-border-radius'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-border-radius'}),
            'message': forms.Textarea(attrs={'class': 'form-control custom-border-radius'}),
        }