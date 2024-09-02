from django.test import TestCase, override_settings

from restaurant.forms import CookCreationForm


class FormsTest(TestCase):
    @override_settings(AUTH_PASSWORD_VALIDATORS=[])
    def test_cook_creation_from_with_correct_data(self):
        form_data = {
            "username": "new_user",
            "email": "new_user@example.com",
            "password1": "79zilivi",
            "password2": "79zilivi",
            "first_name": "new_first_name",
            "last_name": "new_last_name",
            "years_of_experience": 1,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['username'], form_data['username'])
        self.assertEqual(form.cleaned_data['email'], form_data['email'])
        self.assertEqual(form.cleaned_data['first_name'], form_data['first_name'])
        self.assertEqual(form.cleaned_data['last_name'], form_data['last_name'])
        self.assertEqual(form.cleaned_data['years_of_experience'], form_data['years_of_experience'])
