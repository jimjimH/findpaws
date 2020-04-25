from django.contrib import admin
from django.urls import path

from animals.views import (
    animal_list_view,
    animal_detail_view,
)

from animals.views import (
    all_animals_json,
)

app_name = 'animals'

urlpatterns = [
    path('', animal_list_view, name='animal_list'),
    path('<int:id>/', animal_detail_view, name='animal_detail'),


    # test for json respone
    path('all_animals_json', all_animals_json),
]
