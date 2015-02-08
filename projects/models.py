from django.db import models
from django.db.models import Model
from connection.models import *
# Create your models here.


class Objectif (models.Model):
    sujet = models.CharField(max_length=256)

    def __str__(self):
        return self.sujet


class Tag (models.Model):
    nom_tag = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_tag


class Project (models.Model):
    project_id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    objectifs = models.ForeignKey(Objectif,blank=True,null=True)
    tags = models.ForeignKey(Tag,blank=True,null=True)
    status = models.CharField(max_length=9,default='En Cours',blank=True)
    date_depot = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,blank=True,null=True)

    def __str__(self):
        return self.titre