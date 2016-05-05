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
    client = None


class Consultant(Employe):
    missionsEffectues = []


class Client(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    societe = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    emailAdress = models.EmailField("adresse email du client")


        
