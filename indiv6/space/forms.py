from django import forms
from django.apps import apps


def create_model_form(model1):
    class Meta:
        model = model1
        fields = '__all__'

    form_attrs = {'Meta': Meta}
    return type(f'{model1.__name__}Form', (forms.ModelForm,), form_attrs)


def create_forms_for_all_models():
    app_models = apps.get_app_config("space").get_models()
    all_forms = {}

    for model in app_models:
        form = create_model_form(model)
        all_forms[model.__name__] = form

    return all_forms


def create_update_form(model1):
    class DynamicUpdateForm(forms.ModelForm):
        class Meta:
            model = model1
            fields = '__all__'

    return DynamicUpdateForm