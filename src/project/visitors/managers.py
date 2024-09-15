from django.db.models import Manager, QuerySet


class ParentManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_child=False)

class ChildManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_child=True)
