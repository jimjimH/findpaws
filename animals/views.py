from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from animals.models import Animal, Breed, Species, Photo
from django.core import serializers

#For develop/debug
import json
from pprint import pprint
from var_dump import var_dump


def animal_list_view(request):
    animals = Animal.objects.all()
    context = {
        'animals': animals
    }
    return render(request, 'animal_list.html', context)


def animal_detail_view(request, id):
    animal = get_object_or_404(Animal, id=id)
    context = {
        'animal': animal
    }
    return render(request, 'animal_detail.html', context)


def all_animals_json(request):
    animals = Animal.objects.all()
    # return Json: solution1
    animals_json = serializers.serialize(
        'json', animals)
    return HttpResponse(animals_json, content_type='application/json')

    # return Json: solution2
    return JsonResponse({'result': list(animals.values())})
    return JsonResponse(list(animals.values_list()), safe=False)
