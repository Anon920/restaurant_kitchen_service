from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from restaurant.models import Dish, Cook


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
        widget=forms.TextInput(attrs={'placeholder': 'Search by name'}),
    )


class DishSearchForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Search by name'}),
    )


class CookCreationForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
            "email",
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
