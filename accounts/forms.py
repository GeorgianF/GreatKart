from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'password',
            'confirm_password',
        ]

    def __init__(self, *args, **kwarg):
        super(RegistrationForm, self).__init__(*args, **kwarg)
        self.fields[
            'first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields[
            'last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields[
            'phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields[
            'email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields[
            'password'].widget.attrs['placeholder'] = 'Enter Password'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
