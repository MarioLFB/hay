from django import forms
from .models import Table

class TableForm(forms.ModelForm):
    table_capacity = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)], label='Number of people')

    class Meta:
        model = Table
        fields = ['table_capacity', 'table_name', 'table_phone', 'table_email', 'table_date', 'table_time']
        widgets = {
            'table_name': forms.TextInput(attrs={'class': 'form-control'}),
            'table_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'table_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'table_capacity': forms.Select(attrs={'class': 'form-control'}),
            'table_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'table_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
        labels = {
            'table_name': 'Name',
            'table_phone': 'Phone',
            'table_email': 'Email',
            'table_date': 'Date',
            'table_time': 'Time',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.user and Table.objects.filter(user=self.user).exists():
            raise forms.ValidationError("")
        return cleaned_data