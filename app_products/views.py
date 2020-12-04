from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ProductSearchForm

def index(request):
    if request.method == 'POST':
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            searched_food_product =form.cleaned_data.get('search')
            context = {'searched_food_product': searched_food_product}
            print('Dans index:')
            print(context)
            print('----------------------------')
            return render(request, 'results.html', context)
    else:
        form = ProductSearchForm()
        context = {'form': form}
        return render(request, 'index.html', context)


def results(request, context):
    print('Dans result:')
    print(context)
    print('----------------------------')
    return render(request, 'results.html')
