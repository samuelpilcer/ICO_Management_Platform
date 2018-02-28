# coding: utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import sys
from .models import Token

class TokenForm(forms.Form):
    titre = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    symbol = forms.CharField(max_length=3, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cap = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ether_price = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Token
        fields=('titre','description','symbol','cap','ether_price',)