from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView, RedirectView

urlpatterns = (
        [
            path("i18n/", include("django.conf.urls.i18n")),
            path(settings.ADMIN_URL + 'doc/', include('django.contrib.admindocs.urls')),
            path("employees/", include("project.employees.urls")),
        ]
        + i18n_patterns(path(settings.ADMIN_URL, admin.site.urls))
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

# API URLS
# ------------------------------------------------------------------------------
urlpatterns += []

# django-hijack
# ------------------------------------------------------------------------------
# https://django-hijack.readthedocs.io/en/stable/
urlpatterns += [path('hijack/', include('hijack.urls'))]

# DEBUG
# ------------------------------------------------------------------------------
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += []

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

    if "rosetta" in settings.INSTALLED_APPS:
        urlpatterns += [re_path(r"^rosetta/", include("rosetta.urls"))]

