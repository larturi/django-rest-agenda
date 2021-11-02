from django.contrib import admin

from .models import Person, Hobby, Reunion
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

class HobbyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'hobby',
    )

    search_fields = ('hobby',)

class ReunionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'asunto',
        'persona',
        'fecha',
        'hora',
    )

    search_fields = ('asunto', 'persona',)
    list_filter = ('fecha',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(Reunion, ReunionAdmin)
