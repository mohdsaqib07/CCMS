from django.contrib import admin
from .models import Contact

class CustomFields(admin.ModelAdmin):
    fields=['number', 'email', 'concern']


admin.site.register(Contact,CustomFields)
# Register your models here.
