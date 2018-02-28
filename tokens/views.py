# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import requests
import json
import csv
import os
from django.views.static import serve
from .forms import TokenForm
from .models import Token
# Create your views here.


@login_required
def new_token(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            new_token_=Token()
            new_token_.titre=form.cleaned_data.get('titre')
            new_token_.description=form.cleaned_data.get('description')
            new_token_.admin=request.user
            new_token_.symbol=form.cleaned_data.get('symbol')
            new_token_.cap=form.cleaned_data.get('cap')
            new_token_.ether_price=form.cleaned_data.get('ether_price')
            new_token_.save()
            return redirect('home')
    else:
        form = TokenForm()
    return render(request, 'new.html', {'form': form})

@login_required
def token(request, id):
    try:
        token = Token.objects.all().get(id=id)
    except:
        return redirect('home')
    if token.admin!=request.user:
        return redirect('home')

    is_launched=False
    if token.sale_state=="started":
        is_launched=True
    if token.sale_state=="finished":
        is_finished=True

    #tokens=[token]
    id_model=id
    
    return render(request, 'token.html', locals())