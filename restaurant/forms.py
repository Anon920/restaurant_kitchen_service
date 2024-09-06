from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from restaurant.models import Dish, Cook, Ingredient


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Dish
        fields = '__all__'


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Search by dish type name'}),
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Search by dish name'}),
    )


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )

    def clean_years_of_experience(self):
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ['years_of_experience']

    def clean_years_of_experience(self):
        return validate_years_of_experience(
            self.cleaned_data['years_of_experience']
        )


def validate_years_of_experience(years_of_experience):
    if years_of_experience < 0:
        raise forms.ValidationError(
            "You must enter a positive number"
        )

    return years_of_experience


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Search by username'}),
    )


class IngredientForm(forms.ModelForm):
    dishes = forms.ModelMultipleChoiceField(
        required=None,
        queryset=Dish.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientSearchForm(forms.Form):
    ingredient = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Search by ingredient name'}),
    )
