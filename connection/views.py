import logging
from django import template
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from connection.forms import *
from projects.models import *
from random import randint


logger = logging.getLogger(__name__)

#recuperer les données du formulaire
def goToForm(request,formLog=AuthenticationForm):
    logger.error('goToForm exec >>')
    form = formLog(request, data=request.POST)
    formS = UserCreationForm(request.POST)
    #SI connexion
    if 'connect_sub' in request.POST:
        logger.error('LOGIN POST')
        logger.error('form valid ? '+str(form.is_valid()))
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                logger.error(user.username+' is not None')
                if user.is_active:
                    logger.error(user.username+' is active')
                    login(request,user)
                    contextLog = {
                        'user': user,
                    }
                    return HttpResponseRedirect('/home',contextLog)
    #SI incription
    if 'signin_sub' in request.POST:
        logger.error('SIGIN POST')
        logger.error('formS valid ? '+str(formS.is_valid()))
        if formS.is_valid():
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password1')
            userO = User.objects._create_user(username,email,password,False,False)
            userO.first_name = first_name
            userO.save()
            test = SuperUser(user=userO)
            test.save()
            userA = SuperUser.objects.get(user=userO)
            userA.phone = phone
            userA.save()
            userL = authenticate(username=username, password=password)
            contextLog = {
                        'user': userL,
                        'liste': Project.objects.all(),
                    }
            return HttpResponseRedirect('/home',contextLog)
    current_site = get_current_site(request)
    context = {
        'form1': form,
        'form2': formS,
        'site': current_site,
        'site_name': current_site.name
    }
    return TemplateResponse(request, "LibreCoach/index.html", context)





#Retourner à la page d'accueil
def goToHome(request):
    context = {
        'liste': Project.objects.all(),
    }
    return TemplateResponse(request,'LibreCoach/home.html',context)

#Contribuer à un projet
def addProjet(request,num):
    logger.error("test")
    userD = SuperUser.objects.get(user=auth.get_user(request))
    logger.error("test")
    logger.error(num)
    all_p = Project.objects.all()
    temp = Project()
    for t in all_p:
        #logger.error(t.project_id)
        #logger.error(str(num)+'is'+str(int(num) == t.project_id)+'to'+str(t.project_id))
        if (int(num) == t.project_id):
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
    return TemplateResponse(request, "LibreCoach/home.html", context)
