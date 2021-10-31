from django.contrib import admin

from .models import Person
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'job',
        'email',
        'phone',
        'email'
    )

    search_fields = ('full_name', 'email',)
    list_filter = ('job',)

admin.site.register(Person, PersonAdmin)
