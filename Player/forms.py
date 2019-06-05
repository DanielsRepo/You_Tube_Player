from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from bootstrap_modal_forms.forms import BSModalForm
 
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegistrationForm(forms.Form):
    username = forms.CharField(required = True, max_length = 32)
    email = forms.CharField(required = True, max_length = 32)
    password = forms.CharField(required = True, max_length = 32, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        check = User.objects.filter(username=username)

        if check.count():
            raise ValidationError("Username already exists")

        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        check = User.objects.filter(email=email)

        if check.count():
            raise ValidationError("Email already exists")
        else:
            try:
                validate_email(email)
            except ValidationError:
                raise ValidationError("Invalid email address")

        return email
 
    def clean_password(self):
        password = self.cleaned_data.get('password')
 
        if len(password) < 5:
            raise ValidationError("Password must be at least 6 characters long")
 
        return password
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user