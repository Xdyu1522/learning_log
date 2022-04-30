'''
Author: Xie
Date: 2022-04-30 11:38:24
LastEditors: Xie
LastEditTime: 2022-04-30 12:02:55
FilePath: \learning_log\learning_logs\admin.py
Description: 

2022
'''
from django.contrib import admin
from .models import Topic, Entry

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)
