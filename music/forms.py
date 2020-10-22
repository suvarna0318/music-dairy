from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserPlaylist


class RegisterForm(UserCreationForm):
	phone_num=forms.CharField(max_length=10)
	email=forms.EmailField()
	
	class Meta:
		model=User
		fields=['username','email','password1','password2','phone_num']


# class PlaylistCreationForm(forms.ModelForm):
# 	playlist_title=forms.CharField(max_length=200)
	
# 	class Meta:
# 		model=UserPlaylist
# 		fields=['playlist_title']