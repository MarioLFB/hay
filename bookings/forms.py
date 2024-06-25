from .models import Table, Date
from django import forms

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['table_name', 'table_capacity']


class TableDate(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['date_name', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'})
        }