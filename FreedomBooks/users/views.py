from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
import FreedomBooks.settings as sett

class UserLogin(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {
        'title':'Autorization'
    }

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_done')
    extra_context = {
        'title':'Registration'
    }


class RegisterUserDone(TemplateView):
    template_name = 'users/register_200.html'

class LogoutUser(LogoutView):pass

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title':'Profile',
        'default_image':sett.DEFAULT_USER_IMAGE
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')
    
    def get_object(self, queryset = None):
        return self.request.user
    
class UserPassChange(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"


class PasswordChangeDoneViewMofify(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class PassReset(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')

class PassResetDone(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class PassConfirm(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')

class PassResetComplete(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'