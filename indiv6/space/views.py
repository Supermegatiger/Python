from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from .forms import create_forms_for_all_models, create_model_form, create_update_form
from  django.apps import apps


def show_planets(request):
    return render(request, template_name='index.html', context={'div': Planet.objects.all()})


def show_all_forms(request, model_name=None):
    forms = create_forms_for_all_models()
    if request.method == 'POST':
        model = apps.get_model('space', model_name)
        form_class = create_model_form(model)
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('post')
    return render(request, 'post.html', {'forms': forms})


def show_tables(request):
    models_list = apps.get_app_config("space").get_models()

    tables_info = []
    for model in models_list:
        model_info = {
            'model_name': model.__name__,
            'fields': [field.name for field in model._meta.fields],
            'data':  model.objects.all()
        }
        tables_info.append(model_info)

    context = {'tables_info': tables_info}
    return render(request, 'tables.html', context)


def show_update(request, model_name, id=1):

    model = apps.get_model('space', model_name)
    record = get_object_or_404(model, pk=id)

    form_class = create_update_form(model)
    if request.method == 'POST':
        form = form_class(request.POST, instance=record)
        if form.is_valid():
            form.save()
    else:
        form = form_class(instance=record)
    return render(request, 'update.html', {'form': form, 'model_name': model_name, 'id':id})


def db_initialization(request):
    GalaxyType.objects.bulk_create([
        GalaxyType(name='Elliptical'),
        GalaxyType(name='Spiral'),
        GalaxyType(name='Irregular'),
    ])

    # Galaxy
    Galaxy.objects.bulk_create([
        Galaxy(name='Milky Way', age=1.36E10, type_id=2, size=1.0E5),
        Galaxy(name='Andromeda', age=1.32E10, type_id=2, size=1.1E5),
        Galaxy(name='Triangulum', age=1.2E9, type_id=2, size=7.0E3),
    ])

    # StarSystem
    StarSystem.objects.bulk_create([
        StarSystem(name='Solar System', age=4.6E9, radius=4.5E12, galaxy_id=1),
        StarSystem(name='Alpha Centauri', age=4.85E9, radius=1.711E8, galaxy_id=1),
        StarSystem(name='Proxima Centauri', age=4.85E9, radius=1.965E8, galaxy_id=1),
        StarSystem(name='Sirius System', age=2.37E8, radius=1.711E8, galaxy_id=1),
        StarSystem(name='Alpha Centauri B', age=4.85E9, radius=2.187E8, galaxy_id=1),
        StarSystem(name='Kepler-186', age=3.92E9, radius=2.12E8, galaxy_id=2),
    ])

    # Planet
    Planet.objects.bulk_create([
        Planet(name='Earth', age=4.543E9, radius=6.371E6, mass=5.97219E24, habitable=True, system_id=1),
        Planet(name='Mars', age=4.603E9, radius=3.3895E6, mass=6.4171E23, habitable=False, system_id=1),
        Planet(name='Venus', age=4.503E9, radius=6.0518E6, mass=4.8675E24, habitable=False, system_id=1),
        Planet(name='Mars 2', age=4.603E9, radius=3.3895E6, mass=6.4171E23, habitable=False, system_id=2),
        Planet(name='Gliese 581c', age=2.37E9, radius=7.210E6, mass=5.92E24, habitable=True, system_id=4),
        Planet(name='Kepler-186f', age=3.92E9, radius=8.75E6, mass=2.89E24, habitable=True, system_id=6),
    ])

    # Star
    Star.objects.bulk_create([
        Star(name='Sun', temperature=5778, age=4.603E9, radius=6.9634E8, mass=1.989E30, system_id=1),
        Star(name='Proxima Centauri', temperature=3050, age=4.85E9, radius=1.965E8, mass=1.23E28, system_id=3),
        Star(name='Sirius A', temperature=9940, age=2.37E8, radius=1.711E8, mass=2.02E30, system_id=4),
        Star(name='Alpha Centauri A', temperature=5790, age=4.85E9, radius=1.223E9, mass=1.1E30, system_id=2),
        Star(name='Kepler-186 K', temperature=3686, age=3.92E9, radius=3.66E8, mass=0.5E30, system_id=6),
    ])

    return HttpResponse('Данные добавлены')

