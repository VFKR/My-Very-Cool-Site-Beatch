"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class MyRequestForm(forms.Form):
    requestTheme = forms.CharField(max_length=50,
                                   widget=forms.TextInput({
                                       'class' : 'request__theme',
                                       'placeholder' : 'Я хочу поговорить о...'}))

    requestText = forms.CharField(widget=forms.Textarea({
                                      'class' : 'request__text',
                                      'placeholder' : 'Внимательно слушаем'}))

   

    requestMail = forms.EmailField(min_length=7,
                                   widget=forms.TextInput({
                                       'class' : 'request__mail',
                                       'placeholder' : 'Ваш e-mail'}))

    requestRadio = forms.ChoiceField(choices = (
        ('1','Да, супер!'),
        ('2','Больше да, чем нет)'),
        ('3','Больше нет, чем да-.-'),
        ('4','Нет'),
        ), widget=forms.RadioSelect({
            'class' : 'request__radio',

            }),
                                      initial=1
                                      )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text' : 'Комментарий'}
        widgets = {
            'text' : forms.Textarea({'class' : 'comment'})
            }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image')
        labels = {'title': 'Заголовок', 'description' : 'Краткое содержание', 'content' : 'Полное содержание', 'image' : 'Картинка'}
        widgets = { 
            'title' :  forms.TextInput({
                                   'class': 'requesttheme',
                                   'placeholder': 'Заголовок'}),
            'description' :    forms.Textarea({
                                      'class' : 'requesttext',
                                      'placeholder' : 'Краткое содержание'}),
            'content' : forms.Textarea({
                                      'class' : 'request__text',
                                      'placeholder' : 'Текст статьи'}),
            }