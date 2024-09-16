from django.db.models import (PROTECT, CharField, ForeignKey, ManyToManyField,
                              SmallIntegerField)
from django.utils.translation import gettext_lazy as _

from project.utils.models import BaseModel


class SpecialistTypes(BaseModel):
    name = CharField(_("Specialist type name"), max_length=255)

    class Meta:
        db_table = "specialist_types"
        db_table_comment = "Table include data of all specialist types"

        get_latest_by = "update"
        ordering = ("update", "name")

        verbose_name = _("Specialist type")
        verbose_name_plural = _("Specialist types")

    def __str__(self):
        return self.name

class WorkingDays(BaseModel):
    order = SmallIntegerField(_("Working days order"))
    name = CharField(_("Working day name"), max_length=255)
    shortened_name = CharField(_("Shortened name"), max_length=255, default="")

    class Meta:
        db_table = "working_days"
        db_table_comment = "Table include data of working days"

        get_latest_by = "order"
        ordering = ("order",)

        verbose_name = _("Working day")
        verbose_name_plural = _("Working days")

    def __str__(self):
        return self.name

class Employees(BaseModel):
    user = ForeignKey("auth.User", related_name="employees", on_delete=PROTECT)
    specialist_type = ForeignKey(SpecialistTypes, on_delete=PROTECT, verbose_name=_("Specialist type"))
    working_days = ManyToManyField(WorkingDays, verbose_name=_("Working days"), blank=True)

    class Meta:
        db_table = "employees"
        db_table_comment = "Table include data of all employees"

        get_latest_by = "update"
        ordering = ("update", "user")

        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

    def __str__(self):
        return "{type} {full_name}".format(type=self.specialist_type.name, full_name=self.user.get_full_name())
