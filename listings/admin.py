from django.contrib import admin

from .models import Listing

# https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#modeladmin-objects
class ListingAdmin(admin.ModelAdmin):
	
	list_display = ('id','title', 'is_published', 'price', 'list_date', 'realtor')
	list_display_links = ('id', 'title')
	list_filter = (['realtor'])
	list_editable = (['is_published'])
	search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode')
	list_per_page = 50




# Register your models here.
admin.site.register(Listing, ListingAdmin)