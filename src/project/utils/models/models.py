from django.db.models import (DateTimeField,
                              Model)
from django.utils.translation import gettext as _


class BaseModel(Model):
    create = DateTimeField(
        _("Create time"), help_text=_("Timestamp of object create"), blank=True, auto_now_add=True
    )
    update = DateTimeField(
        _("Update time"), help_text=_("Timestamp of object update"), blank=True, auto_now=True
    )

    class Meta:
        abstract = True
