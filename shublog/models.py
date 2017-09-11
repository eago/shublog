# -*- coding: utf-8 -*-
#coding=UTF-8
#from __future__ import unicode_literals

from django.db import models

from DjangoUeditor.models import UEditorField

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=255, verbose_name="Title")
    desc = models.CharField(max_length=128, default='anonymous', editable=False, verbose_name="Description")
    # content = models.TextField(blank=True, null = True,verbose_name = "文章内容")
    Content = UEditorField('content', height=150, width=500, toolbars='normal', blank=True, imagePath="image/",)

    create_date = models.DateTimeField(auto_now_add=False, verbose_name="create_date")
    modify_date = models.DateTimeField(auto_now=True, verbose_name="modify_date")
    is_original = models.BooleanField(default=False, verbose_name="is_original")
    is_publish = models.BooleanField(default=True, verbose_name="is_publish")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
