from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import CustomRegisterView, UserEditProfileView, MyPasswordChangeView, EmailVerify, ResetPasswordView,\
    ResetSuccessView

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('registration/', CustomRegisterView.as_view(), name='registration'),
    # path('activate/<str:token>/', user_activation, name='activate_mail'),
    path('confirm_email/', TemplateView.as_view(template_name='users/registration/confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='email_verify'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/registration/invalid_varify.html'), name='invalid_varify'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path('password/', MyPasswordChangeView.as_view(), name='change_password'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('reset/success/', ResetSuccessView.as_view(), name='reset_success'),


]