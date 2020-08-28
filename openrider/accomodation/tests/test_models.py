from django.test import TestCase
from accomodation.models import Category, Parking, AddAccomodation, Accomodation
from django.contrib.auth.models import User
from django.urls import reverse


class ModelsTest(TestCase):

    def test_category_model(self):
        cat = Category.objects.create(name='gite')
        self.assertEqual(Category.objects.first(), cat)

    def test_cat_string_representation(self):
        cat = Category.objects.create(name='gite')
        self.assertEqual(str(cat), 'gite')

    def test_parking_model(self):
        parking = Parking.objects.create(parking='clos')
        self.assertEqual(Parking.objects.first(), parking)

    def test_parking_string_representation(self):
        parking = Parking.objects.create(parking='clos')
        self.assertEqual(str(parking), 'clos')

    def test_model(self):
        category = Category.objects.create(name="gite")
        parking = Parking.objects.create(parking='clos')
        addAccomodation = AddAccomodation.objects.create(
            addAccomodation_name = "Treulan",
            addAccomodation_category = category,
            addAccomodation_road = "rue du pont",
            addAccomodation_zipcode = "56400",
            addAccomodation_city = "Auray",
            addAccomodation_phone = "0652535455",
            addAccomodation_email = "test@test.fr",
            addAccomodation_parking = parking,
            addAccomodation_description = "Très bien!",
            addAccomodation_statut = "Non_lu"
        )
        self.assertEqual(addAccomodation.addAccomodation_name, "Treulan")
        self.assertEqual(addAccomodation.addAccomodation_category, category)
        self.assertEqual(addAccomodation.addAccomodation_road, "rue du pont")
        self.assertEqual(addAccomodation.addAccomodation_zipcode, "56400")
        self.assertEqual(addAccomodation.addAccomodation_city, "Auray")
        self.assertEqual(addAccomodation.addAccomodation_phone, "0652535455")
        self.assertEqual(addAccomodation.addAccomodation_email, "test@test.fr")
        self.assertEqual(addAccomodation.addAccomodation_parking, parking)
        self.assertEqual(addAccomodation.addAccomodation_description, "Très bien!")
        self.assertEqual(addAccomodation.addAccomodation_statut, "Non_lu")

    def test_string_representation(self):
        category = Category.objects.create(name="gite")
        parking = Parking.objects.create(parking='clos')
        addAccomodation = AddAccomodation.objects.create(
            addAccomodation_name = "Treulan",
            addAccomodation_category = category,
            addAccomodation_road = "rue du pont",
            addAccomodation_zipcode = "56400",
            addAccomodation_city = "Auray",
            addAccomodation_phone = "0652535455",
            addAccomodation_email = "test@test.fr",
            addAccomodation_parking = parking,
            addAccomodation_description = "Très bien!",
            addAccomodation_statut = "Non_lu"
        )
        self.assertEqual(str(addAccomodation), "Treulan")
    
    def test_Accomodation_model(self):
        category = Category.objects.create(name="gite")
        parking = Parking.objects.create(parking='clos')
        user = User.objects.create_user(
            username="UtilisateurTest",
            first_name="utilisateur",
            last_name="Test",
            password="Azertyui4552"
        )
        accomodation = Accomodation.objects.create(
            name = "Treulan",
            category = category,
            road = "rue du pont",
            zipcode = "56400",
            city = "Auray",
            phone = "0652535455",
            email = "test@test.fr",
            park = parking,
            description = "Très bien!",
            lat= '42.121314',
            lon= '2.353637',
        )
        accomodation.likes.add(user)
        utilisateur = User.objects.get(username="UtilisateurTest")
        liked = accomodation.likes.first()
        self.assertEqual(accomodation.name, "Treulan")
        self.assertEqual(accomodation.category, category)
        self.assertEqual(accomodation.road, "rue du pont")
        self.assertEqual(accomodation.zipcode, "56400")
        self.assertEqual(accomodation.city, "Auray")
        self.assertEqual(accomodation.phone, "0652535455")
        self.assertEqual(accomodation.email, "test@test.fr")
        self.assertEqual(accomodation.park, parking)
        self.assertEqual(accomodation.description, "Très bien!")
        self.assertEqual(accomodation.lat, "42.121314")
        self.assertEqual(accomodation.lon, "2.353637")
        self.assertEqual(liked, utilisateur)

    def test_Accomodation_get_absolute_url(self):
        redirect = self.client.get(reverse('accomodation:details', args=['7']))
        self.assertEqual(redirect.status_code, 302)

    def test_Accomodation_str_representation(self):
        category = Category.objects.create(name="gite")
        parking = Parking.objects.create(parking='clos')
        accomodation = Accomodation.objects.create(
            name = "Treulan",
            category = category,
            road = "rue du pont",
            zipcode = "56400",
            city = "Auray",
            phone = "0652535455",
            email = "test@test.fr",
            park = parking,
            description = "Très bien!",
            lat= '42.121314',
            lon= '2.353637',
        )
        self.assertEqual(str(accomodation), "Treulan, None rue du pont, 56400, Auray - 42.121314, 2.353637")
