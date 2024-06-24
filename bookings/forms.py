from .models import Table
from django import forms

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['table_name', 'table_capacity']