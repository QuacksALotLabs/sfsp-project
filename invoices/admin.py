from django.contrib import admin

from invoices.models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    readonly_fields = ("pk", "generated_at")


admin.site.register(Invoice, InvoiceAdmin)