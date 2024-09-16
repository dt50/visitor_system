from django.db.models import (BooleanField, CharField, DateField, EmailField,
                              ManyToManyField, TextField)
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from project.utils.models import BaseModel

from .managers import ChildManager, ParentManager


class Visitor(BaseModel):
    fio = CharField(_("Full name visitor"), max_length=500)
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), blank=True)
    mail = EmailField(_("Mail"), blank=True)
    address = CharField(_("Address"), max_length=500, blank=True)
    is_child = BooleanField(_("Is children?"), default=False)
    parent_problem = TextField(_("Parent problem"), blank=True)

    children = ManyToManyField("visitors.Visitor", verbose_name=_("Children"), related_name="child", blank=True)
    birth_data = DateField(_("Birth date"), null=True, blank=True)

    reason_for_request = TextField(_("Reason for request"), default="", blank=True)

    class Meta:
        db_table = "visitors"
        db_table_comment = "Table include data of all visitors"

        get_latest_by = "update"
        ordering = ("update", "fio")

        verbose_name = _("Visitor")
        verbose_name_plural = _("Visitors")

    def __str__(self) -> str:
        return _("{is_child} - {phone_number}:{full_name} - {count_children} children").format(
            is_child=_("Child") if self.is_child else _("Parent"),
            phone_number=self.phone_number,
            full_name=self.fio,
            count_children=self.children.count(),
        )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs) -> None:
        super().save(force_insert, force_update, using, update_fields)


class Parent(Visitor):
    objects = ParentManager()
    class Meta:
        proxy = True

class Child(Visitor):
    objects = ChildManager()
    class Meta:
        proxy = True
