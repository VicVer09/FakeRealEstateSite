from django.shortcuts import render, get_object_or_404

from .models import Listing
from collections import OrderedDict

from .choices import price_choices, bedroom_choices, state_choices
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# these correspond to urls.py urlpatterns
def index(request):
	
	
	# reverse order (-) and parameter
	# filter removes any objects that don't fit criteria
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)  
	#listings = Listing.objects.all() # returns unordered 
	
	paginator = Paginator(listings, 6)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)
	
	context = {
		
		'listings': paged_listings
	
	}
	
	return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
	
	#function gets item or throws 404 if conditions are not met
	# !!! IMPORTANT, this is in django.shortcuts package
	listing = get_object_or_404(Listing, pk = listing_id)
	
	context = {
	
		'listing': listing
	
	}
	
	return render(request, 'listings/listing.html', context)
	

def search(request):
	
	queryset_list = Listing.objects.order_by('-list_date') 
	
	# ref:
	# https://docs.djangoproject.com/en/2.1/topics/db/queries/#field-lookups
	
	# Keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			# django special xxx__icontains parameter for case-insensitive containment test
			queryset_list = queryset_list.filter(description__icontains=keywords) 
	
	# City
	if 'city' in request.GET:
		city = request.GET['city']
		if city:
			# for case sensitive use __exact
			# django special xxx__iexact parameter for exact match (case insensitive)
			queryset_list = queryset_list.filter(city__iexact=city) 
	
	# State
	if 'state' in request.GET:
		state = request.GET['state']
		if state:
			# for case sensitive use __exact
			# django special xxx__iexact parameter for exact match (case insensitive)
			queryset_list = queryset_list.filter(state__iexact=state) 
	
	# Bedrooms
	if 'bedrooms' in request.GET:
		bedrooms = request.GET['bedrooms']
		if bedrooms:
			# django special xxx__lte for less than or equal to
			queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) 
			
	# Price
	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			# django special xxx__lte same as above
			queryset_list = queryset_list.filter(price__lte=price) 
	
	paginator = Paginator(queryset_list, 6)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page) 
	 
	context = {
	
		'state_choices': state_choices,
		'bedroom_choices': bedroom_choices,
		'price_choices': price_choices,
		'listings': paged_listings,
		'values': request.GET
	}
	
	
	return render(request, 'listings/search.html', context)