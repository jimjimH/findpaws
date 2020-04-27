from django.contrib import admin
from .models import (
    Species, 
    Breed, 
    Animal, 
    Photo, 
    Contact, 
    Footprint,
)

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
        'url',
    ]

class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'identity',
        'name',
        'location',
        'phone',
    ]

class FootprintAdmin(admin.ModelAdmin):
    list_display = [
        'animal_id',
        'contact_id',
        'status',
        'origin',
        'location',
        'start_date',
        'end_date',
    ]

admin.site.register(Species, SpeciesAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Footprint, FootprintAdmin)
