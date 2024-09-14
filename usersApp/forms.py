from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from usersApp.models import User, PC 

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs ={
        'class' : 'w-full border border-gray-300 px-4 py-2 rounded-lg', 'placeholder' : 'Логін'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs ={
        'class' : 'w-full border border-gray-300 px-4 py-2 rounded-lg', 'placeholder' : 'Пароль'
    }))
  
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationFrom(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs ={
        'class' : 'w-full border border-gray-300 px-4 py-2 rounded-lg', 'placeholder' : 'Логін'
    }))

    university = forms.CharField(widget=forms.TextInput(attrs ={
        'class' : 'w-full border border-gray-300 px-4 py-2 rounded-lg', 'placeholder' : 'Університет'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs ={
        'class' : 'w-full border border-gray-300 px-4 py-2 rounded-lg', 'placeholder' : 'Електрона адреса'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs ={
        'class' : 'w-full border border-gray-300 px-4 py-2 rounded-lg', 'placeholder' : 'Введіть ваш пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs ={
        'class' : 'w-full border border-gray-300 px-4 py-2 rounded-lg', 'placeholder' : 'Повторити пароль'
    }))

    class Meta:
        model = User
        fields =('username', 'university', 'email', 'password1', 'password2')

class PCFormAdd(forms.ModelForm):
    class Meta:
        model = PC
        fields = ['institutes_id', 'model', 'inventory_number', 'dateOfPurchase', 'processor', 'RAM', 'video_core', 'office', 'corps']