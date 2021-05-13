"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import MyRequestForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment
from .forms import CommentForm
from .forms import BlogForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Домашняя страница',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Наша страница контактов.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О сайте',
            'message':'Страница с информацией о сайте.',
            'year':datetime.now().year,
        }
    )

def links(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'year':datetime.now().year,
        }
    )

def pool(request):
    """Renders the request page."""
    assert isinstance(request, HttpRequest)
    data = None

    if request.method == 'POST':
        form = MyRequestForm(request.POST)
        if form.is_valid():
            data = dict()
            data['theme'] = form.cleaned_data['requestTheme']
            data['text'] = form.cleaned_data['requestText']
            data['radio'] = form.cleaned_data['requestRadio']
            data['email'] = form.cleaned_data['requestMail']
            form = None
    else:
        form = MyRequestForm()

    return render(
        request,
        'app/pool.html',
        {
            'form' : form,
            'data' : data,
            'title':'Обратная связь',
            'message' : 'Ждём вашего отзыва.',
            'year':datetime.now().year,
        }
    )
def registration(request):

    """Renders the registration page."""

    assert isinstance(request, HttpRequest)

    if request.method == "POST": # после отправки формы

        regform = UserCreationForm (request.POST)

        if regform.is_valid(): #валидация полей формы

            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы

            reg_f.is_staff = False # запрещен вход в административный раздел

            reg_f.is_active = True # активный пользователь

            reg_f.is_superuser = False # не является суперпользователем

            reg_f.date_joined = datetime.now() # дата регистрации

            reg_f.last_login = datetime.now() # дата последней авторизации

            reg_f.save() # сохраняем изменения после добавления данных

            return redirect('home') # переадресация на главную страницу после регистрации

    else:

        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

    return render(

        request,

        'app/registration.html',

        {

        'regform': regform, # передача формы в шаблон веб-страницы

        'year':datetime.now().year,

         }

    )
def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts,
            'year':datetime.now().year,
        }
    )
def blogpost(request, parameter):
    """Renders the blog page."""
    post = Blog.objects.get(id=parameter)
    comments = Comment.objects.filter(post=parameter)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parameter)
            comment_f.save()
            return redirect('blogpost', parameter=post.id)

    else:
        form = CommentForm()



    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {

            'post': post,
            'comments': comments,
            'form': form,
            'year':datetime.now().year,
        }
    )

def newpost(request):

    if request.method == 'POST':
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.author = request.user
            blog_f.posted = datetime.now()
            blog_f.save()
            return redirect('blog')

    else:
        blogform = BlogForm()



    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newpost.html',
        {

            'blogform': blogform,
            'year':datetime.now().year,
        }
    )

def video(request):
  
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Video.html',
        {
            'title':'Видео',
            'year':datetime.now().year,
        }
    )