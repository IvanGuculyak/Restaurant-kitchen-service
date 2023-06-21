from django.shortcuts import render

from service.models import Dish, Ingredient, DishType, Cook


def index(request):
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_ingredients = Ingredient.objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_ingredients": num_ingredients
    }

    return render(
        request,
        "service/index.html",
        context=context
    )
