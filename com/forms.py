from django.forms import ModelForm
from .models import report


class complaint_form(ModelForm):
    class Meta:
        model = report
        fields = '__all__'
