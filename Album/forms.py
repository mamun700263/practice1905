from django import forms
from .models import AlbumModle
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModle
        fields = '__all__'
        widgets={
            'release_date' :forms.DateInput(attrs={'type':'date'}),
        }

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name'];

