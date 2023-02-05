import datetime
import pytz as pytz
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, \
    PasswordResetCompleteView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import CustomEditUserForm, CustomUserCreationForm
from users.models import User
from users.utils import send_verify_email
from django.contrib.auth.tokens import default_token_generator as token_generator

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('catalog:index')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save()
    #         self.object.token = User.objects.make_random_password(length=10)
    #         self.object.token_created = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
    #         self.object.is_active = False
    #         self.object.save()
    #         send_mail(
    #             subject='Активация',
    #             message=f'http://localhost:8000/users/activate/{self.object.token}/',
    #             from_email=settings.EMAIL_HOST_USER,
    #             recipient_list=[self.object.email],
    #             fail_silently=False)
    #
    #     return super().form_valid(form)

# def user_activation(request, token):
#     u = User.objects.filter(token=token).first()
#     if u:
#         self.object.is_active = True
#
#     return redirect(reverse('catalog:index'))

    def get(self, request):
        context = {
            'form': CustomUserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            user.is_active = False
            user.save()
            send_verify_email(request, user)
            return redirect('users:confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class MyPasswordChangeView(PasswordChangeView):
    model = User
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('users:profile')


User = get_user_model()
class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('catalog:index')
        return redirect('invalid_verify')


    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64). decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user


class ResetPasswordView(PasswordResetView):
    model = User
    email_template_name = 'users/password_reset_email.html'
    template_name = 'users/reset_password.html'
    success_url = reverse_lazy('users:reset_success')

    def form_valid(self, form):
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = User.objects.make_random_password(length=10)
            # form.save()
            user = User.objects.filter(email=email).first()
            user.set_password(password)
            user.save()
            # send_mail(
            #     subject='Ваш пароль сброшен',
            #     message=f'Ваш пароль: {password}',
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[email],
            #     fail_silently=False)

        return super().form_valid(form)

class ResetSuccessView(PasswordResetCompleteView):
    template_name = 'users/password_reset_success.html'



