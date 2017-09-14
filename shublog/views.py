# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Article

# Create your views here.

# private methods only used in this file

def get_blog_info(objects):
    blogs_info=[]

    for blog in objects:
        blogs_info.append({
            'title': blog.title,
            'desc': blog.desc,
            'pub_time': blog.create_date,
        })
    return blogs_info

def index(request):
    blogs = Article.objects.all()
    blog_info_list = get_blog_info(blogs)
    content = {
            'blogs_info': blog_info_list
            }
    print blog_info_list
    return render(request, "./index.html", content)