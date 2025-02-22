from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string

from freedombooks_core.models import BookModel, TagsModel, TextModel

# temporary menu
menu = [{'title':'about site', 'url_name':'about'}, 
        {'title':'sign in', 'url_name':'autorise'},
        {'title':'sign up', 'url_name':'register'},
        {'title':'add book', 'url_name':'add'},
        {'title':'get book', 'url_name':'get_book'},
        ]

def main_page(request:HttpRequest):
    posts = {'row':range(8), 'column':range(16)}
    data = {
        'title':'Home',
        'posts':posts,
        'menu':menu
    }
    
    return render(request, 'freedombooks_core/main_page.html', data)
    


def about(request:HttpRequest):
    descr = """
        Welcome to our book site! We're a team of passionate readers and writers who share a love for all things books. 
        From classic literature to the latest bestseller, we strive to provide a wide selection of high-quality books for all reading tastes. 
        We also offer expert recommendations, reading tips, and opportunities to connect with other readers. 
        So whether you're looking for your next great read or simply want to explore the world of books, you've come to the right place. Happy reading!
"""
    data = {
        'title':'about us',
        'menu':menu,
        'description':descr
    }
    return render(request, 'freedombooks_core/about.html', data)

def sign_in(request:HttpRequest):
    descr = 'this is a sign in page'
    data = {
        'title':'sign in',
        'menu':menu,
        'description':descr
    }
    return render(request, 'freedombooks_core/sign_page.html', data)

def sign_up(request:HttpRequest):
    descr = 'this is a sign in page'
    data = {
        'title':'sign up',
        'menu':menu,
        'description':descr

    }
    return render(request, 'freedombooks_core/sign_page.html', data)

def addbook(request:HttpRequest):
    descr = 'this is a add page'
    data = {
        'title':'add book',
        'menu':menu,
        'description':descr

    }
    return render(request, 'freedombooks_core/add_book.html', data)

def get_book(request:HttpRequest):
    posts = BookModel.objects.all()
    descr = 'this is a get_book page'
    data = {
            'title':'get book',
            'menu':menu,
            'description':descr,
            'post':posts
        }

    return render(request, 'freedombooks_core/get_book.html', data)

def get_book_slug(request:HttpRequest, book_slug=None):
    posts = BookModel.objects.get(slug=book_slug)
 
    descr = 'this is a get_book page'
    data = {
            'title':'get book',
            'menu':menu,
            'description':descr,
            'post':posts
        }

    return render(request, 'freedombooks_core/book.html', data)
    


def page_not_found(request:HttpRequest, exception):
    return render(request, 'freedombooks_core/not_found.html')