from django import forms
import django_filters
from .models import DataPersons, CodeBiologyPersontypes

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = DataPersons
        fields = {
            'firstname': ['icontains', ],
            'lastname': ['icontains', ],
            'ethnicityid': ['exact', ],
            'persontypeid': ['exact', ],
        }
