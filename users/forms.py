from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserLoginForm(forms.Form):
    '''
    Form to log in a user to the website using their username and password
    '''
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control custom-border-radius',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control custom-border-radius',
                'placeholder': 'Password'
            }
        )
    )


class UserRegisterForm(forms.Form):
    '''
    Form to register a user to the website using their username,
    email and password
    '''
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control custom-border-radius',
                'placeholder': 'Username'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control custom-border-radius',
                'placeholder': 'Email'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control custom-border-radius',
                'placeholder': 'Password'
            }
        )
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control custom-border-radius',
                'placeholder': 'Confirm Password'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        min_length = 5
        max_length = 20

        if len(username) < min_length:
            raise forms.ValidationError(
                _(
                    'Username must be at least {} characters long.'
                ).format(min_length)
            )
        if len(username) > max_length:
            raise forms.ValidationError(
                _(
                    'Username must be at most {} characters long.'
                ).format(max_length)
            )

        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        min_length = 8

        if len(password) < min_length:
            raise forms.ValidationError(
                _(
                    'Password must be at least {} characters long.'
                ).format(min_length)
            )
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError(
                _(
                    'Password must contain at least one digit.'
                )
            )
        if not any(char.isalpha() for char in password):
            raise forms.ValidationError(
                _(
                    'Password must contain at least one letter.'
                )
            )

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password != password_confirm:
            self.add_error('password_confirm', _('Passwords do not match.'))

        return cleaned_data
