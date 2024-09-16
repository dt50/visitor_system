from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Employees, SpecialistTypes, WorkingDays


@admin.register(SpecialistTypes)
class SpecialistTypesAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("name",)}
        ),
        (
            _("System information"), {"fields": ("create", "update")}
        )
    )

    readonly_fields = ("create", "update")
    list_filter = ("name",)

    list_display = ("name", "employees_count")

    list_per_page = 50

    search_fields = ("name",)

    @admin.display(description=_("Employees"))
    def employees_count(self, obj):
        return Employees.objects.filter(specialist_type=obj.pk).count()


@admin.register(WorkingDays)
class WorkingDaysAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("order", "name", "shortened_name")}
        ),
        (
            _("System information"), {"fields": ("create", "update")}
        )
    )

    readonly_fields = ("create", "update")
    list_filter = ("name",)

    list_display = ("shortened_name", "name")

    list_per_page = 50

    search_fields = ("name",)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("user", "specialist_type", "working_days")}
        ),
        (
            _("System information"), {"fields": ("create", "update")}
        )
    )

    readonly_fields = ("create", "update")
    list_filter = ("user", "specialist_type", "working_days")

    list_display = ("get_full_name", "specialist_type", "get_working_days")

    list_per_page = 50

    search_fields = ("user", "specialist_type", "working_days")

    @admin.display(description=_("Full name"))
    def get_full_name(self, obj):
        return obj.user.get_full_name()


    @admin.display(description=_("Working days"))
    def get_working_days(self, obj):
        return ", ".join([day.shortened_name for day in obj.working_days.all()])