'''
Author: Xie
Date: 2022-04-30 11:38:24
LastEditors: Xie
LastEditTime: 2022-04-30 12:01:40
FilePath: \learning_log\learning_logs\models.py
Description: 

2022
'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model): 
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.text

class Entry(models.Model): 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name_plural = 'entries'

    def __str__(self):   # sourcery skip: assign-if-exp
        if len(self.text) <= 50: 
            return self.text
        else: 
            return f'{self.text[:50]}...'
