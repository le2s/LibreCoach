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


class SuperUser(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10,blank=True)


