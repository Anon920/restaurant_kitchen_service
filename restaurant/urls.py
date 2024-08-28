from django.urls import path

from restaurant import views
from restaurant.views import DishTypeListView, DishListView, DishDetailView, DishCreateView, toggle_assign_to_dish, \
    DishUpdateView, DishDeleteView, DishTypeUpdateView, DishTypeDeleteView, DishTypeCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path("dish_types/", DishTypeListView.as_view(), name='dish-type-list'),
    path("dish_types/create/", DishTypeCreateView.as_view(), name='dish-type-create'),
    path("dish_types/<int:pk>/update", DishTypeUpdateView.as_view(), name='dish-type-update'),
    path("dish_types/<int:pk>/delete", DishTypeDeleteView.as_view(), name='dish-type-delete'),
    path("dishes/", DishListView.as_view(), name='dish-list'),
    path("dish/<int:pk>", DishDetailView.as_view(), name='dish-detail'),
    path("dish/create", DishCreateView.as_view(), name='dish-create'),
    path("dish/<int:pk>/update", DishUpdateView.as_view(), name='dish-update'),
    path("dish/<int:pk>/delete", DishDeleteView.as_view(), name='dish-delete'),
    path("dish/<int:pk>/toggle-assign/", toggle_assign_to_dish, name="toggle-assign-dish"),
    path("cooks/", views.CookListView.as_view(), name='cook-list'),
    path("cook/<int:pk>", views.CookDetailView.as_view(), name='cook-detail'),
    path("cook/create/", views.CookCreateView.as_view(), name='cook-create'),
    path("cook/<int:pk>/update/", views.CookUpdateView.as_view(), name='cook-update'),
    path("cook/<int:pk>/delete", views.CookDeleteView.as_view(), name='cook-delete'),
]

app_name = 'restaurant'
