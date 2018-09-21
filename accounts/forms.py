# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width','placeholder': 'Username'}),
        label='', 
        max_length=30,
        error_messages={ 'max_length': '最大长度为30'},
    )

    
    password = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Password'}),
        label=''
    )
        
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()

        if not user or not user.check_password(password):
            raise forms.ValidationError('用户名或密码不正确')

        return self.cleaned_data    
    

def widget_attrs(placeholder):
    return {'class': 'u-full-width', 'placeholder': placeholder}


def form_kwargs(widget, label='', max_length=64):
    return {'widget': widget, 'label': label, 'max_length': max_length}





class RegistrationForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        label='', 
        max_length=30,
        error_messages={ 'max_length': '最大长度为30'},
    )


    password = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Password'}),
        label=''
    )

    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Password confirmed'}),
        label=''
    )
    
    def validate_user(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if User.objects.filter(username=username).first():
            raise forms.ValidationError('用户名已被使用') 
        if passord != password2:
            raise forms.ValidationError('密码不一致')
        
        return self.cleaned_data
       
