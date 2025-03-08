from django.urls import path
from . import views
# from django.contrib.staticfiles import views as vi
# UpdatePage
# from django.core.mail import send_mail
urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('password-change/',views.UserPassChange.as_view(), name='password_change'),
    path('password-change/done/',views.PasswordChangeDoneViewMofify.as_view(), name='password_change_done'),

    path('password_reset/', views.PassReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PassResetDone.as_view(), name='password_reset_done'),

    path('password_reset/<uidb64>/<token>/', views.PassConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.PassResetComplete.as_view(), name='password_reset_complete'),

    path('register/', views.RegisterUser.as_view(), name='register'),
    path('register_done/', views.RegisterUserDone.as_view(), name='register_done'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
]
