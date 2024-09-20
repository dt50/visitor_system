from django.db.models import (PROTECT, CharField, DateTimeField, ForeignKey,
                              PositiveSmallIntegerField, SlugField, TextField, TimeField, ManyToManyField)
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

from datetime import datetime, timedelta

from project.utils.models import BaseModel
from project.utils.slugify import slugify


class TimeVisits(BaseModel):
    date = ForeignKey("employees.WorkingDays", on_delete=PROTECT, verbose_name=_("Date of visit"))
    time = TimeField(_("Time of visit"))

    def __str__(self):
        return "{day} - {time}".format(day=self.date.shortened_name, time=self.time.strftime("%H:%M"))


class TypeVisit(BaseModel):
    name = CharField(_("Type name"), max_length=255)
    description = TextField(_("Description"))

    slug = SlugField()

    class Meta:
        db_table = "type_visit"
        db_table_comment = "Table include data of all type of visits"

        get_latest_by = "create"
        ordering = ("create",)

        verbose_name = _("Type visit")
        verbose_name_plural = _("Visits types")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        super().save(force_insert=False, force_update=False, *args, **kwargs)


class Session(BaseModel):
    name = CharField(_("Session name"), max_length=255)
    description = TextField(_("Session description"))

    slug = SlugField(unique=True)

    class Meta:
        db_table = "visit_sessions"
        db_table_comment = "Table include data of all visits session"

        get_latest_by = "create"
        ordering = ("create",)

        verbose_name = _("Visit session")
        verbose_name_plural = _("Visits sessions")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        super().save(force_insert=False, force_update=False, *args, **kwargs)


class CompletedSession(BaseModel):
    STATUS = Choices(
        ("held", _("Held")),
        ("not_held", _("Not held"))
    )

    status = CharField(_("Session status"), choices=STATUS, default=STATUS.not_held, max_length=255)
    reason = TextField(_("Session reason"))

    class Meta:
        db_table = "completed_session"
        db_table_comment = "Table include data of all completed sessions"

        get_latest_by = "update"
        ordering = ("update",)

        verbose_name = _("Completed session")
        verbose_name_plural = _("Completed sessions")


class Visits(BaseModel):
    status = Choices(
        ("active", _("Active")),
        ("inactive", _("Inactive")),
    )

    child = ForeignKey("visitors.Child", on_delete=PROTECT, verbose_name=_("Child"))
    accountable = ForeignKey("employees.Employees", on_delete=PROTECT, verbose_name=_("Accountable"))

    time_visit = ManyToManyField(TimeVisits, verbose_name=_("Visits time"))
    type_visit = ForeignKey(TypeVisit, on_delete=PROTECT, verbose_name=_("Visit type"))
    session = ForeignKey(Session, on_delete=PROTECT, verbose_name=_("Session"))
    visits_count = PositiveSmallIntegerField(_("Visits count"), default=1)

    completed_sessions = ManyToManyField(CompletedSession, verbose_name=_("Completed sessions"), blank=True)

    class Meta:
        db_table = "visits"
        db_table_comment = "Table include data of all visits"

        get_latest_by = "update"
        ordering = ("update",)

        verbose_name = _("Visit")
        verbose_name_plural = _("Visits")

    #TODO дописать __str__