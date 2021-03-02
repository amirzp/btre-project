from django.shortcuts import render, get_object_or_404
from .models import Listings
from . import choices
from django.core.paginator import Paginator


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
    querysets = Listings.objects.order_by('-is_data')

    # Keywordsr
    if 'keywordsr' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            querysets = querysets.filter(keywords__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            querysets = querysets.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            querysets = querysets.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            querysets = querysets.filter(bedroom__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            querysets = querysets.filter(price__lte=price)

    context = {
        'state_choices': choices.state_choices,
        'bedroom_choices': choices.bedroom_choices,
        'price_choices': choices.price_choices,
        'listings': querysets,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
