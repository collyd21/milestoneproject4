from django.contrib import admin
from .models import Comp

# Register your models here.


class CompAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'size_range',
        'price',
        'entries',
        'date',
        'image',
    )

    ordering = ('-date',)


admin.site.register(Comp, CompAdmin)
