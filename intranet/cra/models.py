from django.db import models

# Create your models here.


class Employe(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_embauche = models.DateTimeField("date d'embauche")

    def __str__(self):
        return self.nom + "  " + self.prenom


class Consultant(Employe):
    missionsEffectues = []


class Client(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    societe = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    emailAdress = models.EmailField("adresse email du client")

    def __str__(self):
        return self.nom + "  " + self.prenom + " " + self.societe


class Mission_terminee(models.Model):
    dateDebutMission = models.DateTimeField("date de debut de mission")
    poste = models.CharField(max_length=200)
    client = models.ForeignKey(Client)
    dateFinMission = models.DateTimeField("date de fin de mission")
    def __str__(self):
        return self.poste + "  " + self.client + "   " + dateDebutMission + "   " + dateFinMission

class Mission_en_cours(models.Model):
    dateDebutMission = models.DateTimeField("date de debut de mission")
    poste = models.CharField(max_length=200)
    client = models.ForeignKey(Client)
    def __str__(self):
        return self.poste + "  " + self.client
