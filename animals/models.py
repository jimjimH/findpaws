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
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.url


class Contact(models.Model):
    IDENTITY_CHOICES = [
        ('shelter', '收容所'),
        ('abandoner', '送養人'),
        ('owner', '飼主'),
        ('volunteer', '善心人士'),
        ('finder', '發現者'),
        ('other', '其他')
    ]
    identity = models.CharField(max_length=20, choices=IDENTITY_CHOICES)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Footprint(TimeStampMixin):
    ORIGIN_CHOICES = [
        ('shelter', '收容所'),
        ('abandoned', '主人送養'),
        ('lost', '走失訊息'),
        ('stray', '流浪動物'),
    ]
    STATUS_CHOICES = [
        ('open', '可領養'),
        ('sent', '已領養'),
        ('dead', '已過世'),
        ('complete', '已結案'),
        ('unknown', '未知'),

    ]
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    origin = models.CharField(max_length=20, choices=ORIGIN_CHOICES)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return 'animal_id: ' + str(self.animal.id) + ' at ' + str(self.contact.name)
