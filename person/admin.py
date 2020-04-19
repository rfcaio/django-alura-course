from django.contrib import admin

from .models import Person


class PersonList(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('name',)
    list_per_page = 5
    search_fields = ('name',)

admin.site.register(Person, PersonList)
