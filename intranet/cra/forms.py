from django.forms import ModelForm
from .models import Consultant


class ConsultantForm(ModelForm):
    class Meta:
        model = Consultant
        fields = ['nom','prenom']
