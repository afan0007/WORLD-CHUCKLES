# forms.py
from django import forms
from .models import User, History

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'country', 'age', 'gender']
        widgets = {
            'password': forms.PasswordInput(),
        }

class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'country', 'age', 'profile_image', 'gender']

