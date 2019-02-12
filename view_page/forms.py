from django.forms import ModelForm
from .models import Date_info
 
class Date_info_form(ModelForm):
    class Meta:
        model = Date_info
        fields = ['date']
