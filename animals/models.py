from django.db import models
from django.urls import reverse


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Species(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=50)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Animal(TimeStampMixin):
    BODY_SIZE_CHOICES = [
        ('A', '0-3kg'),
        ('B', '3-13kg'),
        ('C', '13-23kg'),
        ('D', '23kg+'),
    ]
    id_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=3)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    fur_color = models.CharField(max_length=20)
    body_size = models.CharField(max_length=3, choices=BODY_SIZE_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    description = models.CharField(max_length=200, blank=True)
    note = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.id) + self.name

    def get_absolute_url(self):
        return reverse("animals:animal_detail", kwargs={"id": self.id})


class Photo(TimeStampMixin):
    animal = models. ForeignKey(Animal, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.url
