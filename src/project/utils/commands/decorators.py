import functools
import sys

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style
from django.utils.translation import gettext as _


def catch_exception(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            stderr = OutputWrapper(sys.stderr)
            style = color_style()
            body = f"""
                \r{_("Caught an exception in")} {f.__name__}
                \r{e}
            """
            stderr.write(style.ERROR(body))
            # TODO configure celery for async send mails about errors
            # send_mail(
            #     "ERROR",
            #     body,
            #     settings.DEFAULT_FROM_EMAIL,
            #     [settings.DEFAULT_FROM_EMAIL],
            #     fail_silently=False,
            # )

    return func
