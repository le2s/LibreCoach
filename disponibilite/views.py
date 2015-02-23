import logging
from django.contrib import auth
from django.shortcuts import render
from django.template.response import TemplateResponse
from connection.models import SuperUser
from disponibilite.forms import *

logger = logging.getLogger(__name__)

#Ajouter/Modifier disponiblite
def goToDispo(request):
    form = DispoInfo(request.POST)
    #status = 'Nouveau Projet'
    logger.error("AHAH")
    userA = SuperUser.objects.get(user=auth.get_user(request))
    if request.method == 'POST':
        logger.error("OK")
        if form.is_valid():
            logger.error("OHHHH")
            result = request.POST
            #logger.error(result)
            lundi = result.get('jour')
            lundi_char = 'lundi'
            mardi = result.get('mardi')
            mardi_char = 'mardi'
            mercredi = result.get('mercredi')
            mercredi_char = 'mercredi'
            jeudi = result.get('jeudi')
            jeudi_char = 'jeudi'
            vendredi = result.get('vendredi')
            vendredi_char = 'vendredi'
            samedi = result.get('samedi')
            samedi_char = 'samedi'
            dimanche = result.get('dimanche')
            dimanche_char = 'dimanche'
            lesjours=[lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche]
            lesjours_char = [lundi_char,mardi_char,mercredi_char,jeudi_char,vendredi_char,samedi_char,dimanche_char]
            count = 0
            obj = Disponibilite()
            for index,e in enumerate(lesjours):
                if(e == 'on'):
                    obj = Disponibilite(jour=lesjours_char[index],user=auth.get_user(request))
                    obj.save()
                    logger.error('new dispo')
                    userA.dispo = obj
                    logger.error('obj define')
                count += 1
    userA.save()
    logger.error('save')
    context = {
        'form': form,
        'userA': SuperUser.objects.get(user=auth.get_user(request))
    }
    return TemplateResponse(request, "LibreCoach/dispo.html", context)
