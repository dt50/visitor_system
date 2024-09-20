from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from project.utils.mixins.premissions import CustomGroupRequiredMixin
from .models import Employees, WorkingDays
from .forms import EmployeeForm

class EmployeeListView(CustomGroupRequiredMixin, ListView):
    required_groups = ["Сотрудник"]

    template_name = "employees/employees_list_view.html"
    model = Employees

    def get_queryset(self):
        self.queryset = (
            Employees.objects.all()
            .select_related("user", "specialist_type")
            .prefetch_related("working_days", "visits_set")
        )
        return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["working_days"] = WorkingDays.objects.all()

        return context


class EmployeeCreateView(CustomGroupRequiredMixin, CreateView):
    required_groups = ["Директор"]

    template_name = "employees/employees_create_view.html"
    model = Employees

    form_class = EmployeeForm

    success_url = reverse_lazy("employees:employees_list")
