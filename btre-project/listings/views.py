from django.shortcuts import render, get_object_or_404
from .models import Listings
from django.core.paginator import Page, PageNotAnInteger, Paginator


def listings(request):
    listings = Listings.objects.all()

    paginator = Paginator(listings, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'listings': page_obj
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
