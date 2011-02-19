import datetime

from django.db import models

from logicaldelete import managers


class Model(models.Model):
    """
    This base model provides date fields and functionality to enable logical
    delete functionality in derived models.
    """
    
    date_created  = models.DateTimeField(default=datetime.datetime.now)
    date_modified = models.DateTimeField(default=datetime.datetime.now)
    date_removed  = models.DateTimeField(null=True, blank=True)
    
    objects = managers.LogicalDeletedManager()
    
    def active(self):
        return self.date_removed == None
    active.boolean = True
    
    def delete(self):
        self.date_removed = datetime.datetime.now()
        self.save()
    
    class Meta:
        abstract = True
