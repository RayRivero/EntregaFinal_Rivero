from django import forms
from .models import Profile, Avatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['avatar']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
