from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe  # noqa: F401
from .models import Recipe
import datetime  # noqa: F401

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