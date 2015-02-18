import logging
from random import randint
from django import template
from django.contrib import auth
from django.template.response import TemplateResponse
from connection import views
from connection.models import *

__author__ = 'Sami'


register = template.Library()


@register.assignment_tag()
def random_number():
    return randint(1,12)

logger = logging.getLogger(__name__)

@register.assignment_tag()
def addProjet(request,num):
    logger.error("test")
    userD = SuperUser.objects.get(user=auth.get_user(request))
    logger.error("test")
    all_p = Project.objects.all()
    temp = Project()
    for t in all_p:
        if (t.project_id == num):
            logger.error("iftest")
            temp = t
            logger.error(temp)
    userD.projet_aide = temp
    # logger.error(SuperUser(request.user).projet_aide)
    userD.save()
    #logger.error(Project.objects.get(project_id=temp.project_id))
    context = {
        'liste': Project.objects.all()
    }
    return TemplateResponse(request, "forms/index.html", context)


