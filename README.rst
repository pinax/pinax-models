Django Logical Delete
=====================

This is a small and simple app that I threw together to get some reuse out of 
something I do in nearly every project and every model I create.  It's too easy
for good data to get deleted and it be unrecoverable.  It's also too easy to
fix this by overriding the model's delete() method and just flagging records
as deleted and then leveraging Django's Managers to override default behavior
so that logically deleted items are not returned in querysets.

There are two exceptions however, that I have found useful to this rule.

#. In the admin I like to see everything with an indicator of whether or not 
   it has been deleted, with the ability to filter down to just active records,
   (or deleted for that matter).
#. I still think it is a valid request when an item is fetched for by it's
   primary key value, that the object should return, even if it is marked as
   deleted.


Installing django-logicaldelete
-------------------------------

::

    pip install django-logicaldelete


Using django-logicaldelete
--------------------------

Using the app is pretty simple:

#. add `logicaldelete` to your INSTALLED_APPS
#. Inherit from `logicaldelete.models.Model` for all models that you wish to 
   share in this functionality.
#. Create and/or Register admins for each of these models using `logicaldelete.admin.ModelAdmin`


Additional
----------

Logical deletes are handled by date stamping a `date_removed` column.  In addition, a `date_created` and `date_modified` columns will be populated as a convenience.


Backwards Incompatible Changes
------------------------------

1.1
***

* Changed `everything` to `all_with_deleted` on LogicalDeleteManager
* LogicalDeleteManager moved from `logicaldelete.models` to `logicaldelete.managers`
* Removed `deleted` and `everything` querysets from `logicaldelete.models.Model`
