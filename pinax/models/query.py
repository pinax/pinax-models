from django.db.models.query import QuerySet


class LogicalDeleteQuerySet(QuerySet):

    def delete(self):
        assert self.query.can_filter(), "Cannot use 'limit' or 'offset' with delete."
        for obj in self.all():
            obj.delete()
        self._result_cache = None
    delete.alters_data = True
