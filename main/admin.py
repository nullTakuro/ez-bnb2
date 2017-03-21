from django.contrib import admin
from .models import user , property, booking

# Register your models here.
admin.site.register(user)
admin.site.register(property)
admin.site.register(booking)
