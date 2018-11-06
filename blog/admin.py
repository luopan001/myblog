# -*- coding: UTF-8 -*-
from django.contrib import admin
from blog.models import BlogsPost,Catagory,Comment,Tag


# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created']

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog','name','email','content','created']

admin.site.register(BlogsPost, BlogsPostAdmin)
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)