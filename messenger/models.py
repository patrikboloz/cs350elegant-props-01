# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class message(models.Model):
    message_subject = models.CharField(max_length=256)
    description = models.TextField()
    email = models.EmailField(max_length=150)
    date = models.DateField(auto_now=True)
    
