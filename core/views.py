from collections import defaultdict

from django.shortcuts import render

from .models import Food


def index(request):
    context = dict()
    return render(request, 'core/index.html', context)


def contact(request):
    context = dict()
    return render(request, 'core/contact.html', context)


def menu(request):
    foods = Food.objects.all()
    food_category = defaultdict(list)
    for food in foods:
        food_category[food.category].append(food)
    context = {"foods": dict(food_category), "food_categories": Food.FOOD_TYPE_CHOICES}
    return render(request, 'core/menu.html', context)
