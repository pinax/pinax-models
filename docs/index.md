# pinax-models


!!! note "Pinax Ecosystem"
    This app was donated to and is a part of the Pinax ecosystem but is just a
    Django app and can be used independently of other Pinax apps.

    To learn more about Pinax, see <http://pinaxproject.com/>


## Quickstart

Install the development version:

    pip install pinax-models

Add `pinax-models` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        "pinax.models",
        # ...
    )


## Logical Deletion

`pinax.models.models.LogicalDeleteModel` aims to provide a consistent interface for
managing logical deletion of models also reducing the need to implement
functionality at the model level.

* Logical Deletion instead of Physical Deletion
* Admin that can reveal which records are "Deleted" and allow you to reverse it.
* Provides some short cuts in the default manager
