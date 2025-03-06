from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from datetime import datetime

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['username''password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class':'form-input'}))
    first_name = forms.CharField(label='Nickname', widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='Email', required=False)
    #year_now = datetime.now().year
    #date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(year_now-120, year_now-0))), required=False)
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'password1', 'password2', 'email']

        widgets = {
            'emai':forms.TextInput(attrs={'class':'form-input'}),
            'first_name':forms.TextInput(attrs={'class':'form-input'})
            }
        
class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Login', widget=forms.TextInput(attrs={'class':'form-input'}), required=False)
    email = forms.EmailField(label='Email', required=False)
    first_name = forms.CharField(label='Nickname', widget=forms.TextInput(attrs={'class':'form-input'}), required=False)
    #year_now = datetime.now().year
    #date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(year_now-120, year_now-0))))
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'email'] # , 'photo', 'date_birth'

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-input'}),
            'email':forms.TextInput(attrs={'class':'form-input'}),
            }
        

class UserPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    new_password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-input'}))