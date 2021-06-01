import django_tables2 as tables
from .models import DataPersons

class PersonTable(tables.Table):
    class Meta:
        model = DataPersons
        template_name = "django_tables2/bootstrap.html"
        fields = {"lastname", "firstname"}
