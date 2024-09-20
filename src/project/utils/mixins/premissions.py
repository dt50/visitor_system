from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin


# GroupRequiredMixin
class GroupRequiredMixin:
    required_groups = []

    def has_group_permissions(self):
        user = self.request.user
        return any(group in user.groups.values_list('name', flat=True) for group in self.required_groups)

    def dispatch(self, request, *args, **kwargs):
        if not self.has_group_permissions():
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class CustomGroupRequiredMixin(GroupRequiredMixin, PermissionRequiredMixin):
    def has_permission(self):
        if self.has_group_permissions():
            return True
        return super(PermissionRequiredMixin, self).has_permission()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the required_groups attribute if not already set
        if not hasattr(self, 'required_groups'):
            self.required_groups = []
