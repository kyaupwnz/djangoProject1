from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator


def send_verify_email(request, user):
    current_site = get_current_site(request)
    context = {
        'domain': current_site.domain,
        'user': user,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user)
    }
    message = render_to_string(
        'users/registration/verify_email.html',
        context=context
    )
    # email = EmailMessage(
    #     'Verify Email',
    #     message,
    #     to=[user.email],
    # )
    # # email.send()
    send_mail(
                subject='Активация',
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False)