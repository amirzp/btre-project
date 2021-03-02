from django.shortcuts import render
from listings.models import Listings
from listings import choices
from realtors.models import Realtor


def index(request):
    lisitngs = Listings.objects.order_by(
        '-is_data'
        ).filter(is_published=True)[:3]

    context = {
        'listings': lisitngs,
        'state_choices': choices.state_choices,
        'bedroom_choices': choices.bedroom_choices,
        'price_choices': choices.price_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_data').all()
    mvp_realtors = Realtor.objects.order_by(
        '-hire_data'
        ).filter(is_mvp=True)[:1]

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
