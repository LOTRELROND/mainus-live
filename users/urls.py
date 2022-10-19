from django.contrib import admin
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path('register/',views.register, name = "register"),
    path('login/',views.loginUser, name = "login"),
    path('logout/',views.logoutUser, name = "logout"), 
    path('activate/<uidb64>/<token>/', views.activate, name = 'activate'),

    # password reset
    path('password_reset/',auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_done/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('password/',auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"))
]