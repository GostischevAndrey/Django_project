from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.conf import settings
from .models import User
from .forms import CustomUserCreationForm, CustomLoginForm


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        user = form.save()

        send_mail(
            subject="Добро пожаловать!",
            message=f"Привет, {user.username}!\n\nСпасибо за регистрацию на нашем сайте.\n\nВаш email: {user.email}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        from django.contrib.auth import login

        login(self.request, user)

        return super().form_valid(form)


class UserLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "users/login.html"
