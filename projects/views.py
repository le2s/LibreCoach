import logging
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse
from projects.models import *
from projects.forms import *

# Create your views here.

logger = logging.getLogger(__name__)


def goToProjet(request):
    form = ProjectCreate(request.POST)
    status = 'Nouveau Projet'
    logger.error('SIGIN ')
    if request.method == 'POST':
            logger.error('SIGIN POST >>')
            logger.error('formS valid ? '+str(form.is_valid()))
            if form.is_valid():
                titre = request.POST.get('titre')
                t = request.POST.get('tag')
                obj = request.POST.get('objectif')
                ts = request.POST.get('tags')
                objs = request.POST.get('objectifs')
                user = auth.get_user(request)
                if (t != '') & (obj != ''):
                    objectif = Objectif(sujet=obj)
                    objectif.save()
                    logger.error('objectif save ok')
                    tags = Tag(nom_tag=t)
                    tags.save()
                    logger.error('tags save ok')
                    projet = Project(titre=titre,objectifs=objectif,tags=tags,user=user)
                    projet.save()
                    logger.error('projet save ok')
                    status = 'Projet créer'
                    return HttpResponseRedirect('/home')
                if (ts != '') & (objs != ''):
                    logger.error('spinner')
                    projet = Project(titre=titre,objectifs=Objectif(objs),tags=Tag(ts),user=user)
                    projet.save()
                    logger.error('projet2 save ok')
                    statue = 'Projet créer'
                    return HttpResponseRedirect('/home')
                if (ts != '') & (objs == '') & (obj != ''):
                    objectif= Objectif(sujet=obj)
                    objectif.save()
                    projet = Project(titre=titre,objectifs=objectif,tags=Tag(ts),user=user)
                    projet.save()
                    logger.error('projet3 save ok')
                    statue = 'Projet créer'
                    return HttpResponseRedirect('/home')
                if (ts == '') & (objs != '') & (t != ''):
                    tags = Tag(nom_tag=t)
                    tags.save()
                    projet = Project(titre=titre,objectifs=Objectif(objs),tags=tags,user=user)
                    projet.save()
                    logger.error('projet4 save ok')
                    statue = 'Projet créer'
                    return HttpResponseRedirect('/home')
    current_site = get_current_site(request)
    context = {
        'form': form,
        'site': current_site,
        'site_name': current_site.name,
        'status': status,
        'liste': Project.objects.all()
        }
    #return render_to_response("forms/index.html",{"form1": form}, context_instance=RequestContext(request))
    return TemplateResponse(request, "LibreCoach/projet.html", context)


