from django.contrib import admin
from .models import SpecialistTypes, WorkingDays, Employees
from django.utils.translation import gettext_lazy as _


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
            {"fields": ("fio", "specialist_type", "working_days")}
        ),
        (
            _("System information"), {"fields": ("create", "update")}
        )
    )

    readonly_fields = ("create", "update")
    list_filter = ("fio", "specialist_type", "working_days")

    list_display = ("fio", "specialist_type", "get_working_days")

    list_per_page = 50

    search_fields = ("fio", "specialist_type", "working_days")

    @admin.display(description=_("Working days"))
    def get_working_days(self, obj):
        return ", ".join([day.shortened_name for day in obj.working_days.all()])