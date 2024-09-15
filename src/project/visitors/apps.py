from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VisitorsConfig(AppConfig):
    name = "project.visitors"
    verbose_name = _("Visitors")
