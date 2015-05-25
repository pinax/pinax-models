Pinax Models
============

On May 25, 2015, Patrick donated `django-logicaldelete` to Pinax and as part of
that process, `pinax-models` was born and the code incorporated into that
package. It remains just a Django app and can be quite independently of other
Pinax apps.

To learn more about Pinax, see http://pinaxproject.com/

.. image:: https://img.shields.io/travis/pinax/pinax-models.svg
    :target: https://travis-ci.org/pinax/pinax-models

.. image:: https://img.shields.io/coveralls/pinax/pinax-models.svg
    :target: https://coveralls.io/r/pinax/pinax-models

.. image:: https://img.shields.io/pypi/dm/pinax-models.svg
    :target:  https://pypi.python.org/pypi/pinax-models/

.. image:: https://img.shields.io/pypi/v/pinax-models.svg
    :target:  https://pypi.python.org/pypi/pinax-models/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://pypi.python.org/pypi/pinax-models/

This is a small and simple app that Patrick Altman wrote to get some reuse out
of something he did in nearly every project and every model he created.  It's
too easy for good data to get deleted and it be unrecoverable.  It's also too
easy to fix this by overriding the model's delete() method and just flagging
records as deleted and then leveraging Django's managers to override default
behavior so that logically deleted items are not returned in querysets.

There are two exceptions to this rule, however, that are useful.

#. In the admin it is nice to see everything with an indicator of whether or not
   it has been deleted, with the ability to filter down to just active records,
   (or deleted for that matter).
#. It is a valid request when an item is fetched by its primary key value, that
   the object should return, even if it is marked as deleted.


Installing pinax-models
-----------------------

::

    pip install pinax-models


Using pinax-models
------------------

Using the app is pretty simple:

#. add `pinax.models` to your INSTALLED_APPS
#. Inherit from `pinax.models.LogicalDeleteModel` for all models that you wish
   to share in this functionality.
#. Create and/or Register admins for each of these models using
   `pinax.models.LogicalDeleteModelAdmin`


Additional
----------

Logical deletes are handled by date stamping a `date_removed` column.  In
addition, a `date_created` and `date_modified` columns will be populated as a
convenience.


Backwards Incompatible Changes
------------------------------

2.0
***

* Renamed to `pinax-models` and base model renamed to `LogicalDeleteModel`


1.1
***

* Changed `everything` to `all_with_deleted` on LogicalDeleteManager
* LogicalDeleteManager moved from `logicaldelete.models` to `logicaldelete.managers`
* Removed `deleted` and `everything` querysets from `logicaldelete.models.Model`
