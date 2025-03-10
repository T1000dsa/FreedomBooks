from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView, ListView
from freedombooks_core.forms import AddPostBook, UploadClassForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .utils import DataMixin
from freedombooks_core.models import BookModel, TagsModel
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from freedombooks_core.services import TextLoad
# venv/Scripts/activate | deactivate; venv -> 1 | 0
# pip install -U aiogram; -U when venv: 1 | -U if venv == True
# git add <file> | git add .
# git commit -m "disciption"
# git push origin main
# python3 -m venv venv
# venv/Scripts/activate.bat
# ./venv/Scripts/activate
# virtualenv .env
# git ls-files | xargs wc -l
# python manage.py runserver -O port

menu = [{'title':'about site', 'url_name':'about'}, 
        #{'title':'sign in', 'url_name':'autorise'},
        #{'title':'sign up', 'url_name':'register'},
        {'title':'add book', 'url_name':'add'},
        {'title':'get book', 'url_name':'get_books'},
        ]


class IndexHome(DataMixin, ListView):
    model = BookModel
    template_name = 'freedombooks_core/main_page.html'
    title_page = 'home'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            contex,
            index_list=contex['bookmodel_list'])
    
class AboutPage(DataMixin, TemplateView):
    template_name = 'freedombooks_core/about.html'
    title_page = 'about'
    descr = """
        Welcome to our book site! We're a team of passionate readers and writers who share a love for all things books. 
        From classic literature to the latest bestseller, we strive to provide a wide selection of high-quality books for all reading tastes. 
        We also offer expert recommendations, reading tips, and opportunities to connect with other readers. 
        So whether you're looking for your next great read or simply want to explore the world of books, you've come to the right place. Happy reading!
        """

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            contex,
            description = self.descr)
'''
class SignInPage(DataMixin, TemplateView):
    template_name = 'freedombooks_core/sign_page.html'
    title_page = 'sign in'
    descr = 'this is a sign in page'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            contex,
            description = self.descr)

class SignUpPage(DataMixin, TemplateView):
    template_name = 'freedombooks_core/sign_page.html'
    title_page = 'sign up'
    descr = 'this is a sign in page'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            contex,
            description = self.descr)
'''

    
class AddBookNew(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = AddPostBook
    template_name = 'freedombooks_core/add_book.html'
    permission_required = 'freedombooks_core.add'
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'adding'
        return contex
    

class UpdateBook(PermissionRequiredMixin, LoginRequiredMixin,  UpdateView):
    model = BookModel
    fields = "__all__"
    template_name = 'freedombooks_core/book_update.html'
    success_url = reverse_lazy('home_page')
    permission_required = 'freedombooks_core.update'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'editing'
        return contex


class GetBooks(DataMixin, ListView):
    model = BookModel
    template_name = 'freedombooks_core/get_book.html'
    title_page = 'Choice the book!'

    def get_queryset(self):
        return BookModel.objects.all()
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            contex,
            post=contex['bookmodel_list'],
            description = 'this is a get_book page')
    
class GetBook(DataMixin, ListView):
    model = BookModel
    template_name = 'freedombooks_core/book.html'
    title_page = 'Good reading!'

    def get_queryset(self):
        return BookModel.objects.filter(slug=self.kwargs['book_slug'])
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        data = contex['bookmodel_list'][0]
        text_view = 'No text'

        if data.text_hook:
            text_data = TextLoad(data)
            text_view = text_data.push_text()
            

        return self.get_mixin_context(contex, 
                                      title=data.title,
                                      post=data,
                                      content=text_view)

class DeleteBook(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = BookModel
    template_name = 'freedombooks_core/delete_page.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home_page')
    permission_required = 'freedombooks_core.delete_book'
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'delete'
        return contex


def page_not_found(request:HttpRequest, exception):
    return render(request, 'freedombooks_core/not_found.html')