"""
Definition of urls for lab013.
"""


from datetime import datetime
from django.urls import path,re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('links/', views.links, name='links'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('pool/',views.pool,name='pool'),
    path('registration', views.registration, name='registration'),
    path('blog/',views.blog,name='blog'),
    re_path(r'^(?P<parameter>\d+)/$', views.blogpost, name='blogpost'),
    path('newpost/',views.newpost,name='newpost'),
    path('video/',views.video,name='video'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()