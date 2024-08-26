from django.test import TestCase, override_settings

from restaurant.forms import CookCreationForm

class FormsTest(TestCase):
    @override_settings(AUTH_PASSWORD_VALIDATORS=[])
    def test_cook_creation_from_with_correct_data(self):
        form_data = {
            "username": "test",
            "password1": "Password1test",
            "password2": "Password2test",
            "first_name": "test_first",
            "last_name": "test_last",
            "years_of_experience": 1,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form.data)
