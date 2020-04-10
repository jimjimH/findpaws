from django.db import models

# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Breed(models.Model):
    breed_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)

class Animal(TimeStampMixin):
    id_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=20)
    breed = models.ForeignKey("Breed", on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=3)
    age = models.PositiveSmallIntegerField()
    fur_color = models.CharField(max_length=20)
    body_size = models.CharField(max_length=3)
    description = models.CharField(max_length=200, blank=True)
    note = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


