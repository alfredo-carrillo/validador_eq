from django.shortcuts import render
from django_registration.backends.activation.views import ActivationView as BaseActivationView
from django_registration.backends.activation.views import RegistrationView as BaseRegistrationView
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.core.mail import send_mail

from django.conf import settings



# Create your views here.
class RegistrationView(BaseRegistrationView):

    def send_activation_email(self, user):
       """
       Send the activation email. The activation key is the username,
       signed using TimestampSigner.

       """
       activation_key = self.get_activation_key(user)
       context = self.get_email_context(activation_key)
       context["user"] = user
       subject = render_to_string(
           template_name=self.email_subject_template,
           context=context,
           request=self.request,
       )
       # Force subject to a single line to avoid header-injection
       # issues.
       subject = "".join(subject.splitlines())
       message = render_to_string(
           template_name=self.email_body_template,
           context=context,
           request=self.request,
       )
       # user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

       send_mail(
           subject,
           '',
           settings.DEFAULT_FROM_EMAIL,
           [user.email],
           html_message=message,
           fail_silently=False,
       )


class ActivationView(BaseActivationView):
    pass