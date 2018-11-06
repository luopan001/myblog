# -*- coding: UTF-8 -*-
from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label='称呼',max_length=16,error_messages={
        'required':'请填写您的称呼',
        'max_length':'称呼过长'
    })

    email = forms.EmailField(label='邮箱',error_messages={
        'required':'请填写您的邮箱',
        'invalid':'邮箱格式错误'
    })

    content = forms.CharField(label='评论',error_messages={
        'required': '请填写您的评论',
        'max_length': '评论内容过长'
    })