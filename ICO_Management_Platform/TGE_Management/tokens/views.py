# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
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
            new_model=Token()
            new_model.titre=form.cleaned_data.get('titre')
            new_model.description=form.cleaned_data.get('description')
            new_model.admin=request.user
            new_model.save()
            return redirect('home')
    else:
        form = TokenForm()
    return render(request, 'new.html', {'form': form})

@login_required
def token(request, id):
    try:
        model = Token.objects.all().get(id=id)
    except:
        return redirect('home')
    if model.admin!=request.user:
        return redirect('home')

    models=[model]
    id_model=id
    
    return render(request, 'model.html', locals())