from .models import Table
from django import forms

class TableForm(forms.ModelForm):
    table_capacity = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)], label='Number of people')

    class Meta:
        model = Table
        fields = ['table_name', 'table_phone', 'table_email', 'table_capacity', 'table_date', 'table_time']
        widgets = {
            'table_date': forms.DateInput(attrs={'type': 'date'}),
            'table_time': forms.TimeInput(attrs={'type': 'time'}),
        }

        labels = {
            'table_name': 'Name',
            'table_phone': 'Phone',
            'table_email': 'Email',
            'table_date': 'Date',
            'table_time': 'Time',
        }
