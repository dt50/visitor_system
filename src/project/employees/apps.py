from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmployeesConfig(AppConfig):
    name = "project.employees"
    verbose_name = _("Employees")
