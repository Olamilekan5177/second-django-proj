from django import forms
from django.contrib.auth.models import User


class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

class CustomSignUpForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")

        return cleaned_data
    
# class ProfileEditForm(forms.Form):
#     email = forms.EmailField(label="Email")
#     bio = forms.CharField(widget=forms.Textarea, label="Bio", required=False)
#     location = forms.CharField(max_length=100, label="Location", required=False)
#     username = forms.CharField(max_length=150, label="Username")
class ProfileEditForm(forms.Form):
    email = forms.EmailField(label="Email")
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # Optional: Add Bootstrap or custom classes
            'style': 'height: 150px; resize: none;',  # Fixed height for the textarea
            'placeholder': 'Tell us about yourself...',  # Optional placeholder
        }),
        label="Bio",
        required=False,
    )
    location = forms.CharField(max_length=100, label="Location", required=False)
    username = forms.CharField(max_length=150, label="Username")
