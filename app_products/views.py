from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProductSearchForm
from app_products.models import FoodProductsManager, FoodProduct
from app_users.models import UsersManager
from django.contrib.auth import get_user_model

fp_manager = FoodProductsManager()
u_manager = UsersManager()
context = { 'search_form': ProductSearchForm() }

def index(request):
    return render(request, 'index.html', context)

def search(request):
    if request.method == 'POST':
        search_form = ProductSearchForm(request.POST)
        if search_form.is_valid():
            searched_product = search_form.cleaned_data.get('search')
            matching_list = fp_manager.find_matching_food_products(
                searched_product)
            context = { 'searched_product': searched_product,
                        'matching_list':  matching_list }
            return render(request, 'search.html', context)
    return render(request, 'search.html', context)

def substitutes(request, selected_product_id):
    product_to_substitute = fp_manager.find_product_by_id(selected_product_id)
    substitutes_list = fp_manager.find_substitutes(product_to_substitute)
    context = { 'product_to_substitute': product_to_substitute,
                'substitutes_list':  substitutes_list }
    return render(request, 'substitutes.html', context)

def product_details(request, selected_product_id):
    product_to_display = fp_manager.find_product_by_id(selected_product_id)
    context = { 'product_to_display': product_to_display}
    return render(request, 'product_details.html', context)

@login_required()
def favorites(request, product_to_save_id = None):
    """get current user"""
    User = get_user_model()
    current_user = request.user
    product_to_save = None
    current_user_favorites_list = u_manager.get_favorites_list(current_user)
    if product_to_save_id != None:
        product_to_save = fp_manager.find_product_by_id(product_to_save_id)
        if product_to_save in current_user_favorites_list:
            messages.error(request,'déja dans vos favorits' )
        else:
            u_manager.add_to_favorites_list(current_user,product_to_save)
            messages.success(request,'ajouté à vos favorits' )
            current_user_favorites_list = u_manager.get_favorites_list(
                current_user)
    context = { 'product_to_save': product_to_save,
                'current_user_favorites_list':  current_user_favorites_list }
    return render(request, 'favorites.html', context)

def legal_disclaimers(request):
    return render(request, 'legal_disclaimers.html', context)
