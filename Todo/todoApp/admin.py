from django.contrib import admin
from .models import *


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["created_date","completed"]
    search_fields = ["title"]

admin.site.register(Todo,TodoAdmin)

