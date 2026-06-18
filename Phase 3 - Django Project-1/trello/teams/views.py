from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Teams
from .forms import TeamForm


class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return (
            self.request.user.is_superuser
            or self.request.user.role == "MANAGER"
        )


class TeamCreateView(LoginRequiredMixin, ManagerRequiredMixin, CreateView):
    model = Teams
    form_class = TeamForm
    template_name = "teams/team_form.html"
    success_url = reverse_lazy("team-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class Team_List_view(LoginRequiredMixin, ListView):
    model = Teams
    template_name = "teams/team_list.html"
    context_object_name = "teams"
    paginate_by = 2


class Team_Detail_View(LoginRequiredMixin, DetailView):
    model = Teams
    template_name = "teams/details_page.html"
    context_object_name = "team"


class TeamUpdateView(LoginRequiredMixin, ManagerRequiredMixin, UpdateView):
    model = Teams
    form_class = TeamForm
    template_name = "teams/team_form.html"
    success_url = reverse_lazy("team-list")


class TeamDeleteView(LoginRequiredMixin, ManagerRequiredMixin, DeleteView):
    model = Teams
    template_name = "teams/team_confirm_delete.html"
    success_url = reverse_lazy("team-list")