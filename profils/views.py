import logging
from django.contrib import auth
from django.shortcuts import render
from connection.models import *

# Create your views here.
from django.template.response import TemplateResponse


def goToProfil(request):
    logger = logging.getLogger(__name__)
    context = {
        'userA': SuperUser.objects.get(user=auth.get_user(request)),
        'projetA': Project.objects.filter(user=auth.get_user(request))
    }
    logger.error(SuperUser.objects.get(user=auth.get_user(request)).level)
    return TemplateResponse(request, "LibreCoach/profil.html", context)