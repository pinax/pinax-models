from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', '__unicode__', 'active')
    list_display_filter = ('active',)

    def queryset(self, request):
        qs = self.model._default_manager.everything()
        ordering = self.ordering or ()
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
