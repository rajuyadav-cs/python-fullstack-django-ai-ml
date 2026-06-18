from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm

from teams.models import Teams
from projects.models import Project
from tasks.models import Task


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")


class Login(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard")


class Logout(LogoutView):
    next_page = "login"


class DashBoard(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_teams"] = Teams.objects.count()
        context["total_projects"] = Project.objects.count()
        context["total_tasks"] = Task.objects.count()
        context["completed_tasks"] = Task.objects.filter(status="DONE").count()
        context["pending_tasks"] = Task.objects.exclude(status="DONE").count()

        context["my_tasks"] = Task.objects.filter(
            assigned_to=self.request.user
        ).count()

        context["recent_tasks"] = Task.objects.all().order_by("-created_at")[:5]

        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"