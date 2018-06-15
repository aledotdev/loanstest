import requests
from django.forms import ModelForm

from .models import LoanRequest


class LoanRequestForm(ModelForm):
    class Meta:
        model = LoanRequest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LoanRequestForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def is_approved(self):
        url = 'http://scoringservice.moni.com.ar:7001/api/v1/scoring/'
        params = {
            'document_number': self.cleaned_data['dni'],
            'gender': self.cleaned_data['gender'],
            'email': self.cleaned_data['email']
        }

        response = requests.get(url, params=params)

        is_approved = response.json().get('approved') is True
        has_erros = response.json().get('error') is False

        return is_approved and has_erros
