from django import forms
from .models import Pano
from .models import Tour
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PanoForm(forms.ModelForm):
    class Meta:
        model = Pano
        fields = ('title', 'location', 'p', )

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('tour_title', 'tour_location')

# class SceneForm(forms.Form):
#     s_title = forms.CharField(max_length=200)
#     s_caption = forms.CharField(max_length=200)
#     sf = forms.FileField()
#     tf = forms.IntegerField()

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
