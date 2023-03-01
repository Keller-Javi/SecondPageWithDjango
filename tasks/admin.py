from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', )

# Register your models here.
admin.site.register(Task, TaskAdmin)

# Superuser
# User: JaviK
# pas: Javi5000