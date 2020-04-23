from django.contrib import admin
from .models import Species, Breed, Animal, Photo

# Register your models here.
class SpeciesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
class BreedAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

class AnimalAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'id_number',
        'name',
        'breed_id',
        'gender',
        'age',
        'fur_color',
        'body_size',
    ]

class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'animal_id',
        'description',
    ]

admin.site.register(Species, SpeciesAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Photo, PhotoAdmin)
