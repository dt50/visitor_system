from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VisitsConfig(AppConfig):
    name = "project.visits"
    verbose_name = _("Visits")
