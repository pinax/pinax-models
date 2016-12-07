# -*- coding: utf-8 -*-

import itertools

from django.db import DEFAULT_DB_ALIAS

from django.contrib.admin.utils import NestedObjects


def get_related_objects(obj, using=DEFAULT_DB_ALIAS):
    # This code is based on https://github.com/makinacorpus/django-safedelete
    collector = NestedObjects(using=using)
    collector.collect([obj])

    def flatten(elem):
        if isinstance(elem, list):
            return itertools.chain.from_iterable(map(flatten, elem))
        elif obj != elem:
            return (elem,)
        return ()

    return flatten(collector.nested())
