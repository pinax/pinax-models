try:
    from django.utils import timezone
except ImportError:
    from datetime import datetime as timezone

from django.db import models

from logicaldelete import managers


class Model(models.Model):
    """
    This base model provides date fields and functionality to enable logical
    delete functionality in derived models.
    """

    date_created  = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    date_removed  = models.DateTimeField(null=True, blank=True)

    objects = managers.LogicalDeletedManager()

    def active(self):
        return self.date_removed is None
    active.boolean = True

    def delete(self):
        self.date_removed = timezone.now()
        self.save()

    class Meta:
        abstract = True
