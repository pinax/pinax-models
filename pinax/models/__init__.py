import pkg_resources

from .admin import LogicalDeleteModelAdmin  # noqa
from .models import LogicalDeleteModel  # noqa


__version__ = pkg_resources.get_distribution("pinax-models").version
