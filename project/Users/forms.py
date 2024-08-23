# forms.py
from django import forms
from .models import User
from django.core.exceptions import ValidationError

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
        fields = ['username', 'password', 'country', 'age', 'gender', 'profile_image']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_id = self.instance.id  # Get the id of the current user being updated

        # Check if a user with the same username exists but not the current user
        if User.objects.filter(username=username).exclude(id=user_id).exists():
            raise ValidationError("This username is already taken. All update failed")
        return username

