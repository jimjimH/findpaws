from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from animals.models import Animal, Breed, Species
from django.core import serializers

#For develop/debug
import json
from pprint import pprint
from var_dump import var_dump


def animal_list_view(request):
    animals = Animal.objects.all()
    var_dump(Animal.objects.get(id=1))

    context = {
        'animals': animals
    }
    return render(request, 'animal_list.html', context)


def all_animals_json(request):
    animals = Animal.objects.all()
    # return Json: solution1
    animals_json = serializers.serialize(
        'json', animals)
    return HttpResponse(animals_json, content_type='application/json')

    # return Json: solution2
    return JsonResponse({'result': list(animals.values())})
    return JsonResponse(list(animals.values_list()), safe=False)
