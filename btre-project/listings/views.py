from django.shortcuts import render, get_object_or_404
from .models import Listings


def listings(request):
    listings = Listings.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context=context)


def listing(request, listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
