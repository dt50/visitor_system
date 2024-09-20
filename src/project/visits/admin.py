from datetime import datetime

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from project.utils.admin.utils import model_admin_url
from django.utils.html import linebreaks

from .models import Session, TypeVisit, Visits, TimeVisits, CompletedSession
from .forms import TimeVisitsForm


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None, {
                "fields": ("name", "description"),
            }
        ),
        (
            _("System information"), {"fields": ("create", "update", "slug")}
        )
    ]

    readonly_fields = ("create", "update", "slug")
    list_filter = ("name", "description")

    list_display = ("name", "description", "slug")

    list_per_page = 50

    search_fields = ("name", "description")


@admin.register(TypeVisit)
class TypeVisitAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, {
                "fields": ("name", "description")
            }
        ),
        (
            _("System information"), {"fields": ("create", "update", "slug")}
        )
    )

    readonly_fields = ("create", "update", "slug")
    list_filter = ("name", "description")

    list_display = ("name", "description", "slug")

    list_per_page = 50

    search_fields = ("name", "description")


@admin.register(TimeVisits)
class TimeVisitsAdmin(admin.ModelAdmin):
    form = TimeVisitsForm

    fieldsets = (
        (
            None, {
                "fields": ("date", "time")
            }
        ),
        (
            _("System information"), {"fields": ("create", "update")}
        )
    )

    readonly_fields = ("create", "update")
    list_filter = ("date", "time")

    list_display = ("date", "time")

    list_per_page = 50

    search_fields = ("date", "time")


@admin.register(CompletedSession)
class CompletedSessionAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, {
                "fields": ("status", "reason")
            }
        ),
        (
            _("System information"), {"fields": ("create", "update")}
        )
    )

    readonly_fields = ("create", "update")
    list_filter = ("status", "reason")

    list_display = ("status", "reason")

    list_per_page = 50

    search_fields = ("status", "reason")


@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, {
                "fields": ("child", "accountable", "type_visit", "session", "visits_count", "time_visit", )
            }
        ),
        (
            _("Completed sessions"), {
                "fields": ("completed_sessions",)
            }
        ),
        (
            _("System information"), {"fields": ("create", "update")}
        )
    )

    readonly_fields = ("create", "update")
    list_filter = ("child__fio", "accountable__specialist_type__name", "type_visit__name", "session__name")

    list_display = ("child", "accountable", "type_visit", "session", "visits_count", "get_visits_times")

    list_per_page = 50

    search_fields = ("child__fio", "accountable__specialist_type__name", "session__name")

    filter_horizontal = ("time_visit",)

    @admin.display(description="Visits time")
    def get_visits_times(self, obj):
        times = []
        cur_day_num = datetime.today().weekday()

        for i in obj.time_visit.all().order_by("date__order"):
            if i.date.order == cur_day_num+1:
                times.append("<span class='text-danger'>{day} - {time}</span>".format(
                    day=i.date.shortened_name,
                    time=i.time.strftime("%H:%M")
                ))
            else:
                times.append("{day} - {time}".format(
                    day=i.date.shortened_name,
                    time=i.time.strftime("%H:%M")
                ))


        return mark_safe(linebreaks("\n".join(times)))
