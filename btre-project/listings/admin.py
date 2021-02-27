from django.contrib import admin
from .models import Listings


class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'is_published',
        'price',
        'is_data',
        'realtor'
    )
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    search_fields = (
        'id',
        'title',
        'address',
        'city',
        'state',
        'zipcode',
        'price',
        'descriptions'
    )
    list_editable = ('is_published', )
    list_per_page = 25


admin.site.register(Listings, ListingAdmin)
