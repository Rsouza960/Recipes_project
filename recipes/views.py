from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe
import datetime  # noqa: F401
from django.http.response import Http404
from django.db.models import Q

def home(request):  # noqa: E302
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')
    return render(request, "recipes/pages/home.html", context={
        "recipes": recipes,
        })

def category(request, category_id):  # noqa: E302

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )


    return render(request, "recipes/pages/category.html", context={  # noqa: E303, E501
        "recipes": recipes,
        'title': f'{recipes[0].category.name} - Category |'
        })


def recipe(request, id):  # noqa: E501, E303
    recipe = get_object_or_404(Recipe, pk=id,
                               is_published=True, )
    return render(request, "recipes/pages/recipe-view.html", context={
        "recipe": recipe,
        'is_detail_page': True,
        })  # noqa: W292


def search(request):
    search_term = request.GET.get('q', '').strip()  # o strip elimina os espaços desnecessarios

    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |   #'i' ele ignora se for maiuscula ou minuscula
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')
    
    return render(request, 'recipes/pages/search.html', context={
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': recipes, 
    })