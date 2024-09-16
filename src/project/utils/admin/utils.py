from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.db.models import Model
from django.shortcuts import resolve_url
from django.utils.html import format_html
from django.utils.safestring import SafeText


def model_admin_url(obj: Model, name: str = None) -> str:
    url = resolve_url(admin_urlname(obj._meta, SafeText("change")), obj.pk)
    return format_html(
        '<a href="{}">{}</a>', url, name or str(obj)
    )
