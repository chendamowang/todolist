#-*- coding: utf-8 -*-
from django import forms

class TodoListForm(forms.Form):
    title = forms.CharField(label='事项', max_length=128)
