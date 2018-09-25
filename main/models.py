# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class TodoList(models.Model):
    title = models.CharField(max_length=128, default='untitled')
    created_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True, related_name='todolists', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return self.title
