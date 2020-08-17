from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name

class Parking(models.Model):
    parking = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.parking


class Accomodation(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    road = models.CharField(max_length=250)
    zipcode = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    url = models.CharField(max_length=200, null=True, blank=True)
    lat = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    park = models.ForeignKey(Parking, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}, {} - {}, {}'.format(self.name, self.road, self.zipcode, self.city, self.lat, self.lon)

class AddAccomodation(models.Model):
    addAccomodation_category_list = (
        ("hotel", "Hotel"),
        ("gite", "Gite"),
        ("bnb", "BnB"),
    )

    addAccomodation_parking_list = (
        ("garage", "Garage"),
        ("couvert", "Couvert"),
        ("ferme", "Fermé"),
    )

    addAccomodation_statut_list = (
        ("Non_lu", "Non lu"),
        ("Lu", "Lu"),
        ("Archive", "Archivé"),
    )

    addAccomodation_name = models.CharField("Nom", max_length=128)
    addAccomodation_category = models.CharField("Catégorie", choices=addAccomodation_category_list, max_length=16)
    addAccomodation_number = models.PositiveSmallIntegerField("Numéro", null=True, blank=True)
    addAccomodation_road = models.CharField("Adresse", max_length=248)
    addAccomodation_zipcode = models.PositiveIntegerField("Code Postal")
    addAccomodation_city = models.CharField("Ville", max_length=50)
    addAccomodation_phone = models.BigIntegerField("Téléphone")
    addAccomodation_email = models.EmailField("Email")
    addAccomodation_url = models.URLField("URL", null=True, blank=True)
    addAccomodation_parking = models.CharField("Type de parking", choices=addAccomodation_parking_list, max_length=16)
    addAccomodation_statut = models.CharField("Statut de la demande", choices=addAccomodation_statut_list, max_length=16, default="Non_lu")

    def __str__(self):
        return '{}'.format(self.addAccomodation_name)