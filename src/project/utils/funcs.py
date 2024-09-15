import time
from collections.abc import Callable
from typing import Any, Iterable, Union

from django.conf import settings
from django.urls import get_resolver


def current_milli_time() -> int:
    return round(time.time() * 1000)


def get_paths() -> Iterable[str]:
    return [
        resolver.__dict__["pattern"].__dict__["_route"]
        for resolver in get_resolver().url_patterns
        if resolver.__dict__["pattern"].__dict__.get("_route", "") != ""
    ]


def function_call(state: bool, func: Callable, *args: Any, **kwargs) -> Any:
    if state:
        return func(*args, **kwargs)


def get_link2site(path: str) -> str:
    domain = settings.APP_URL

    return "{domain}{path}".format(domain=domain, path=path)


def file_name_shortener(file_name: str) -> str:
    base_name = file_name[:file_name.find(".")]

    if len(base_name) > 30:
        base_name = "".join(base_name[:25])
        extension = file_name[file_name.find("."):]

        return base_name + "..." + extension

    return file_name


def delete_from_string(string: str, replacements: Iterable) -> str:
    for replacement in replacements:
        string = string.replace(replacement, "")
    return string


def get_percent(part: Union[int, float], whole: Union[int, float]) -> float:
    return float(whole) / 100 * float(part)
