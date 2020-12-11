from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.contrib.auth.decorators import login_required
from .forms import ProductSearchForm
from app_products.models import FoodProduct
from django.contrib.auth import get_user_model

def index(request):
    context = {'search_form': ProductSearchForm()}
    return render(request, 'index.html', context)

def search(request):
    if request.method == 'POST':
        search_form = ProductSearchForm(request.POST)
        if search_form.is_valid():
            searched_product =search_form.cleaned_data.get('search')
            matching_list = search_for_matching_products_to(searched_product)
            context = { 'search_form': ProductSearchForm(),
                        'searched_product': searched_product,
                        'matching_list':  matching_list }
            return render(request, 'search.html', context)

def substitutes(request, selected_product_id):
        product_to_substitute = get_object_or_404(  FoodProduct,
                                                    id=selected_product_id)
        substitutes_list = search_for_substitutes_to(product_to_substitute)
        context = { 'search_form': ProductSearchForm(),
                    'product_to_substitute': product_to_substitute,
                    'substitutes_list':  substitutes_list }
        return render(request, 'substitutes.html', context)

def product_details(request, selected_product_id):
    product_to_display = get_object_or_404(
                                FoodProduct, id=selected_product_id)
    context = { 'search_form': ProductSearchForm(),
                'product_to_display': product_to_display}
    return render(request, 'product_details.html', context)

@login_required()
def favorites(request, product_to_save_id=''):
    """get current user"""
    User = get_user_model()
    current_user = request.user
    current_user_favorites_list = []
    message = ''
    if product_to_save_id:
        #get product to save
        product_to_save = get_object_or_404(FoodProduct,id=product_to_save_id)
        #Associate the product with current user
        if current_user.favorites.filter(id=product_to_save.id).exists():
            messages.error(request,
                    product_to_save.product_name + ' déja dans vos favorits' )
        else:
            current_user.favorites.add(product_to_save)
            messages.success(request,
                    product_to_save.product_name + ' ajouté à vos favorits' )

    current_user_favorites_list = current_user.favorites.all()
    context = { 'search_form': ProductSearchForm(),
                'message': message,
                'current_user_favorites_list':  current_user_favorites_list }
    return render(request, 'favorites.html', context)


def search_for_matching_products_to(searched_product):
    """ get the corresponding food products in database """
    vector = SearchVector('product_name')
    query = SearchQuery(searched_product)
    matching_list = FoodProduct.objects.annotate(search=vector
                ).filter(search=query
                ).order_by('product_name')
    if len(matching_list)>8:
        matching_list = matching_list[:9]
    return matching_list

def search_for_substitutes_to(product_to_substitute):
    """ select the products with the most common categories
        with the product to be substituted and better nutriscore"""
    substitutes_list= []
    product_to_substitute_categories = product_to_substitute.categories.all()
    product_to_substitute_nutriscore = product_to_substitute.nutriscore

    """ annotate :  annotate products with sum of common categories with
                    the product to be substituted
        filter: categories identical to those of the product to be substituted
                and nutriscor lower than that of the product to be substituted
        order : decreasing number of categories in common
                and increasing nutriscore value
    """
    substitutes_list = FoodProduct.objects.annotate(
                    common_categories=Count('categories')
        ).filter(   categories__in=product_to_substitute_categories,
                    nutriscore__lt=product_to_substitute_nutriscore
        ).order_by('-common_categories', 'nutriscore')
    """ keeps only 9 results """
    if len(substitutes_list)>8:
        substitutes_list = substitutes_list[:9]
    return substitutes_list
