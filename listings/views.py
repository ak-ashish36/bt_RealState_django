from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices


# Create your views here.
def index(request):
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {"listings": paged_listings}
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": listing}
    return render(request, "listings/listing.html",context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    search_field = request.GET.dict()

    if search_field['keywords']:
        queryset_list =queryset_list.filter(description__icontains=search_field['keywords'])
    if search_field['city']:
        queryset_list =queryset_list.filter(city__iexact=search_field['city'])
    if 'state' in search_field.keys() and search_field['state']:
        queryset_list =queryset_list.filter(state__iexact=search_field['state'])
    if 'bedrooms' in search_field.keys() and  search_field['bedrooms']:
        queryset_list =queryset_list.filter(bedrooms__lte=search_field['bedrooms'])
    if 'price' in search_field.keys() and search_field['price']:
        queryset_list =queryset_list.filter(price__lte=search_field['price'])

    context = {
        "listings": queryset_list,
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        'values':request.GET
    }
    return render(request, "listings/search.html",context)
