from django.contrib import admin
from .models import Visitor, Parent, Child
from django.utils.translation import gettext_lazy as _
from .forms import VisitorForm
from django.utils.safestring import mark_safe
from django.urls import reverse
from project.utils.admin.utils import model_admin_url
from datetime import datetime


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    form = VisitorForm
    fieldsets = (
        (
            None,
            {"fields": ("fio", "birth_data", "phone_number", "mail", "address", "is_child", "children", "parent_problem",)}
        ),
        (
            _("Problem"),
            {"fields": ("reason_for_request",)}
        ),
        (
            _("System information"), {"fields": ("create", "update")}
        )
    )

    readonly_fields = ("create", "update")
    list_filter = ("fio", "phone_number", "mail", "address", "is_child")
    
    list_display = ("fio", "age", "is_child", "phone_number", "mail", "address", "get_children_count", "parent")

    list_per_page = 50

    search_fields = ("fio", "phone_number", "mail", "address", "is_child")

    @admin.display(description=_("Age"), ordering="birth_data")
    def age(self, obj):
        if not obj.birth_data:
            return None
        now = datetime.now()
        return now.date().year - obj.birth_data.year

    @admin.display(description="Children count", ordering="children")
    def get_children_count(self, obj):
        if not obj.is_child:
            return obj.children.count()
        else:
            return None

    @admin.display(description=_("Parent"), ordering="fio")
    def parent(self, obj):
        if obj.is_child:
            display = Visitor.objects.get(children=obj.pk)
            return model_admin_url(obj=display, name=display.fio)
        else:
            return None


@admin.register(Parent)
class ParentAdmin(VisitorAdmin):
    list_display = ("fio", "age", "phone_number", "mail", "address", "get_children_count")


@admin.register(Child)
class ChildAdmin(VisitorAdmin):
    list_display = ("fio", "age", "parent", "reason_for_request")
