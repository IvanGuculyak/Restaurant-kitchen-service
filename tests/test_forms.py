from django.test import TestCase

from service.forms import CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_additional_fields_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 123
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)