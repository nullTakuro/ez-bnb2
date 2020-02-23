from django.contrib import admin
from .models import property, contract, tenant, document, tax_payment, rent_payment

admin.site.register(property)
admin.site.register(contract)
admin.site.register(tenant)
admin.site.register(document)
admin.site.register(tax_payment)
admin.site.register(rent_payment)
