from django.contrib.auth.forms import UserChangeForm, UserCreationForm, SetPasswordForm
from catalog.forms import StyleFormMixin
from users.models import User


class CustomEditUserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ("email", 'avatar', 'phone_number', 'country')


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
