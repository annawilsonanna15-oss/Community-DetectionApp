from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input-box',
            'placeholder': 'Email Address'
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Username'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-box',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-box',
            'placeholder': 'Confirm Password'
        })
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            "profile_image",
            "phone",
            "department"
        ]

        widgets = {

            "phone": forms.TextInput(attrs={
                "class": "input-box",
                "placeholder": "Phone Number"
            }),

            "department": forms.TextInput(attrs={
                "class": "input-box",
                "placeholder": "Department"
            }),

        }