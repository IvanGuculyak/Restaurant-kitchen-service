from django.shortcuts import render
from django.views import generic

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


class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 5


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "service/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 3


class DishDetailView(generic.DetailView):
    model = Dish


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 3


class CookDetailView(generic.DetailView):
    model = Cook
