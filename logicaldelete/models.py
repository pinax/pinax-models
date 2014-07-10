import datetime

from django.db import models

from logicaldelete import managers


class Model(models.Model):
    """
    This base model provides date fields and functionality to enable logical
    delete functionality in derived models.
    """

    date_created = models.DateTimeField(default=datetime.datetime.now)
    date_modified = models.DateTimeField(default=datetime.datetime.now)
    date_removed = models.DateTimeField(null=True, blank=True)

    objects = managers.LogicalDeletedManager()

    def active(self):
        return self.date_removed == None
    active.boolean = True

    def delete(self):
        '''
        Soft delete all fk related objects that
        inherit from logicaldelete class
        '''

        # Fetch related models
        related_objs = [relation.get_accessor_name() for
                        relation in self._meta.get_all_related_objects()]

        for objs_model in related_objs:
            # Retrieve all related objects
            objs = getattr(self, objs_model).all()

            for obj in objs:
                # Checking if inherits from logicaldelete
                if not issubclass(obj.__class__, Model):
                    break
                obj.delete()

        # Soft delete the object
        self.date_removed = timezone.now()
        self.save()

    class Meta:
        abstract = True
