from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
class CreateNewUser(UserCreationForm):
    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Your Email'})
    )

    username = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Your Username'})
    )

    password1 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
    )

    password2 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation'})
    )
    
    
    class Meta:
        model = User
        fields = ('email','username','password1','password2')


class EditProfile(forms.ModelForm):
    dob = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={'type':'date',})
    )
    class Meta:
        model = UserProfile
        exclude = ('user',)







from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username','password1','password2')
