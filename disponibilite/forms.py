from django.forms import ModelForm
from django import forms
from connection.models import Disponibilite
__author__ = 'Sami'


class DispoInfo(ModelForm):
    jour = forms.BooleanField(label='lundi')
    mardi = forms.BooleanField(label='mardi',required=False)
    mercredi = forms.BooleanField(label='mercredi',required=False)
    jeudi = forms.BooleanField(label='jeudi',required=False)
    vendredi = forms.BooleanField(label='vendredi',required=False)
    samedi = forms.BooleanField(label='samedi',required=False)
    dimanche = forms.BooleanField(label='dimanche',required=False)

    class Meta:
        model = Disponibilite
        fields = {'jour',}