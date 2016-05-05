from django.db import models

# Create your models here.
class Employe(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_embauche = models.DateTimeField("date d'embauche")

    def __str__(self):
        return self.nom + "  " + self.prenom

class Mission(models.Model):
    nomClient = models.CharField(max_length=200)
    dateDebutMission = models.DateTimeField("date de debut de mission") 
    dateFinMission = models.DateTimeField("date de fin de mission")

class Consultant(Employe):
    missionsEffectues = []

class Mission(models.Model):
    date_debut = models.DateField("Date de début de mission")
    date_fin = models.DateField("Date de fin de mission")
    client = Client

class Client(models.Model):n
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    societe = models.CharField(max_length=200)

        
