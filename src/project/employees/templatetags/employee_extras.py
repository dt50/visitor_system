from typing import Hashable, Mapping, Any
from django.template.defaulttags import register


@register.filter
def get_working_time(dictionary:Mapping, key:Hashable) -> Any:
    return dictionary.get(key, None)
