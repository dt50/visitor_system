from django.contrib import admin
from .models import Visitor, Parent, Child
from django.utils.translation import gettext_lazy as _
from .forms import VisitorForm
from django.utils.safestring import mark_safe
from django.urls import reverse
from project.utils.admin.utils import model_admin_url


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    form = VisitorForm
    fieldsets = (
        (
            None,
            {"fields": ("fio", "phone_number", "mail", "address", "is_child", "children")}
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
    
    list_display = ("fio", "is_child", "phone_number", "mail", "address", "get_children_count", "parent")

    list_per_page = 50

    search_fields = ("fio", "phone_number", "mail", "address", "is_child")

    @admin.display(description="Children count", ordering="children")
    def get_children_count(self, obj):
        if not obj.is_child:
            return obj.children.count()
        else:
            return None

    @admin.display(description=_("Parent"))
    def parent(self, obj):
        if obj.is_child:
            display = Visitor.objects.get(children=obj.pk)
            return model_admin_url(obj=display, name=display.fio)
        else:
            return None


@admin.register(Parent)
class VisitorAdmin(VisitorAdmin):
    pass


@admin.register(Child)
class VisitorAdmin(VisitorAdmin):
    pass