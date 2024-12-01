from django import forms
from .models import Table
from datetime import datetime, date, timedelta


TIME_CHOICES = []
start_time = datetime.strptime('11:30', '%H:%M')
end_time = datetime.strptime('22:00', '%H:%M')

current_time = start_time
while current_time <= end_time:
    time_str = current_time.strftime('%H:%M')
    display_time = current_time.strftime('%I:%M %p')
    TIME_CHOICES.append((time_str, display_time))
    current_time += timedelta(minutes=30)


class TableForm(forms.ModelForm):
    '''
    Form for the Table model, used for booking a table
    '''
    table_capacity = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 11)],
        label='Number of people'
    )

    table_time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control custom-border-radius'}
        ),
        label='Time'
    )

    class Meta:
        model = Table
        fields = [
            'table_capacity', 'table_name', 'table_phone',
            'table_email', 'table_date', 'table_time'
        ]
        widgets = {
            'table_name': forms.TextInput(
                attrs={'class': 'form-control custom-border-radius'}
            ),
            'table_phone': forms.TextInput(
                attrs={'class': 'form-control custom-border-radius'}
            ),
            'table_email': forms.EmailInput(
                attrs={'class': 'form-control custom-border-radius'}
            ),
            'table_capacity': forms.Select(
                attrs={'class': 'form-control custom-border-radius'}
            ),
            'table_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control custom-border-radius',
                    'min': date.today().strftime('%Y-%m-%d')
                }
            ),
        }
        labels = {
            'table_name': 'Name',
            'table_phone': 'Phone',
            'table_email': 'Email',
            'table_date': 'Date',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.user and Table.objects.filter(user=self.user).exists():
            raise forms.ValidationError(
                "You have already booked a table."
            )

        table_date = cleaned_data.get('table_date')
        table_time = cleaned_data.get('table_time')

        if table_time:
            table_time_obj = datetime.strptime(table_time, '%H:%M').time()
            cleaned_data['table_time'] = table_time_obj

        if table_date == date.today() and table_time:
            now = datetime.now().time()
            if table_time_obj < now:
                raise forms.ValidationError(
                    "Reservations for past dates are not allowed. Please choose a future time."
                )

        return cleaned_data
