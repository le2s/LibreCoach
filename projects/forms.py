from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render
from connection.models import *
from projects.models import Project
from django.forms import ModelForm


class ProjectCreate(ModelForm):
    titre = forms.CharField(label="Titre", help_text='Titre')
    objectif = forms.CharField(label="Objectifs", required=False, help_text="Objectif")
    tag = forms.CharField(label="Tags", required=False, help_text="Tag")

    class Meta:
        model = Project
        fields = ("titre","objectif","tag","objectifs","tags",)
