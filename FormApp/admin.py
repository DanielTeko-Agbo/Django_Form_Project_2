from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Form 

class FormAdmin(ImportExportModelAdmin):
    list_display = ['name', 'gender', 'car', 'date']
    list_filter = ['gender', 'date']
    ordering = (('date'),)

admin.site.register(Form, FormAdmin)
