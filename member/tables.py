import django_tables2 as tables
from member.models import Cheque_details
class Cheque_details_table(tables.Table):
    class Meta:
        model = Cheque_details
        template_name = "django_tables2/bootstrap.html"