from django.forms import ModelForm
from .models import Person
from .models import Snack


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'lname', 'money']


class SnackForm(ModelForm):
    class Meta:
        model = Snack
        fields = ['name', 'amount', 'price']
