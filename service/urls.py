from django.urls import path
from service.views import (
    index,
    IngredientListView,
    DishTypeListView,
    DishListView,
    CookListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "ingredients/",
        IngredientListView.as_view(),
        name="ingredient-list"
    ),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    )
]

app_name = "service"