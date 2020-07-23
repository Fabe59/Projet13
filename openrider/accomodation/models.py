from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name

class Parking(models.Model):
    parking = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.parking


class Accomodation(models.Model):
    name = models.CharField(max_length=200, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(blank=True)
    road = models.CharField(max_length=250)
    zipcode = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    park = models.ForeignKey(Parking, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.zipcode, self.city)

