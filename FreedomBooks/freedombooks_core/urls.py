"""
URL configuration for FreedomBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from freedombooks_core import views
urlpatterns = [
    path('', views.IndexHome.as_view(), name='home_page'),
    path('about_site/', views.AboutPage.as_view(), name='about'),
    #path('sign_up/', views.SignUpPage.as_view(), name='register'),
    #path('sign_in/', views.SignInPage.as_view(), name='autorise'),
    path('add_book/', views.AddBookNew.as_view(), name='add'),
    path('get_books/', views.GetBooks.as_view(), name='get_books'),
    path('change_book/<int:pk>/', views.UpdateBook.as_view(), name='update'),
    path('get_book/<slug:book_slug>/', views.GetBook.as_view(), name='get_by_slug'),
    path('delete_book/<int:pk>/', views.DeleteBook.as_view(), name='delete_book'),
    
]

