# Django Logical Delete

This is a small and simple app that I threw together to get some reuse out of 
something I do in nearly every project and every model I create.  It's too easy
for good data to get deleted and it be unrecoverable.  It's also too easy to
fix this by overriding the model's delete() method and just flagging records
as deleted and then leveraging Django's Managers to override default behavior
so that logically deleted items are not returned in querysets.

There are two exceptions however, that I have found useful to this rule.

1. In the admin I like to see everything with an indicator of whether or not 
   it has been deleted, with the ability to filter down to just active records,
   (or deleted for that matter).
2. I still think it is a valid request when an item is fetched for by it's
   primary key value, that the object should return, even if it is marked as
   deleted.

## Using django-logicaldelete

Using the app is pretty simple:

1. Put the logicaldelete sub-folder in your Python Path.
2. Inherit from `logicaldelete.models.Model` for all models that you wish to 
   share in this functionality.
3. Create and/or Register admins for each of these models using `logicaldelete.admin.ModelAdmin`

## Additional

Logical deletes are handled by date stamping a `date_removed` column.  In addition, a `date_created` 
and `date_modified` columns will be populated as a convenience.

## Possible Extensions

You can easily subclass these two classes to provide generic and useful functionality
to your models.  

### UUID Primary Key

I typically using UUID fields for my primary keys because they enable
me to shard my tables if and when I need to, in addition, they provide an obfuscated 
id to my data (people can't determine how many of a certain object I have in my database, 
if I don't want them to know, but simply looking an an integer id in the URL).

### Sequence Field

Many times I find it useful to have an integer field on my models that allow for and explicitly
controlled sequencing.  I normally implement this as a sort descending implementation where the
data is sorted from high to low by sequence value.

In order to to implement this you'd subclass both the Model and ModelAdmin, where the Model 
would be an obvious simple addition of an IntegerField, the ModelAdmin, would override `get_query_set`,
to do something like:


    class SequencedModel(logicaldelete.models.Model):
        sequence = models.IntegerField()
    
    
    class MyLogicalDeletedManager(logicaldelete.models.LogicalDeletedManager):
        def get_query_set(self):
            if self.model:
                qs = super(MyLogicalDeletedManager, self).get_query_set().filter(date_removed__isnull=True)
                if SequencedModel in inspect.getmro(self.model):
                    qs = qs.order_by('-sequence')
                return qs

