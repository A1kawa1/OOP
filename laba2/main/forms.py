from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from main.models import Dictionary


class DictionaryForm(forms.ModelForm):
    class Meta:
        model =Dictionary
        fields = ('word', 'translation')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Такая пара уже существует",
            }
        }
