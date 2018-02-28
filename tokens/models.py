# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Token(models.Model):
    titre = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    cap = models.IntegerField(default=1000000)
    ether_price = models.FloatField(default=1)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    sale_state = models.CharField(max_length=100, default="not_started")
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de parution")
    #address = models.CharField(max_length=100, default="0")
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.titre
