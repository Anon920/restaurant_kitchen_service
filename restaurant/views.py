from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.test.client.RequestFactory import generic

import restaurant
from restaurant.forms import DishTypeSearchForm
from restaurant.models import Cook, Dish, DishType


# Create your views here.


def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_cooks': num_cooks,
        'num_dishes': num_dishes,
        'num_dish_types': num_dish_types,
        'num_visits': num_visits + 1,
    }

    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = 'dish_types'
    template_name = 'restaurant/dish_type_list.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.session.get('name', '')
        context["search_form"] = DishTypeSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = DishTypeSearchForm(self.request.GET)
        queryset = DishType.objects.all()
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset



