from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on')
    search_fields = ('name', 'email', 'body')


admin.site.register(Review, ReviewAdmin)
