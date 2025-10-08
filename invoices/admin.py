from django.contrib import admin

from invoices.models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    readonly_fields = ("pk", "generated_at")

# registers a model to the admin interface
admin.site.register(Invoice, InvoiceAdmin)