from django.forms import ModelForm
from .models import AddAccomodation


class AddAccomodationForm(ModelForm):

    class Meta:
        model = AddAccomodation
        fields = ['addAccomodation_name', 'addAccomodation_category', 'addAccomodation_number', 'addAccomodation_road', 'addAccomodation_zipcode', 'addAccomodation_city', 'addAccomodation_phone', 'addAccomodation_email', 'addAccomodation_url', 'addAccomodation_image', 'addAccomodation_parking']