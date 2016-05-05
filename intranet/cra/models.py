from django.db import models

# Create your models here.
class Employe(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_embauche = models.DateTimeField('date published')
