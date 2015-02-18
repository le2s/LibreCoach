from django.contrib.auth.models import User
from django.db import models
from projects.models import Project
# Create your models here.



class ContactF(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    motdepasse = models.CharField(max_length=10)


    def __str__(self):              # __unicode__ on Python 2
        return self.prenom+' '+self.nom


class Disponibilite(models.Model):
    jour = models.CharField(max_length=15)
    user = models.ForeignKey(User,blank=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.user.username +' le '+ self.jour


class SuperUser(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10,blank=True)
    level = models.IntegerField(max_length=10,default=1,blank=True)
    projet_aide = models.ForeignKey(Project,blank=True,null=True)
    dispo = models.ForeignKey(Disponibilite,blank=True,null=True)


