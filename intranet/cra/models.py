from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Employe(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_embauche = models.DateField("date d'embauche")
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    class Meta:
        abstract = True
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
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return self.nom + "  " + self.prenom + " " + self.societe

class Commercial(Employe):
    liste_consultants = models.ManyToManyField(Consultant,null=True,blank=True)
    liste_clients = models.ManyToManyField(Client,null=True,blank=True)

class Commercial2(Employe):
    liste_consultants = []
    liste_clients = []

class Mission_terminee(models.Model):
    dateDebutMission = models.DateTimeField("date de debut de mission")
    poste = models.CharField(max_length=200)
    client = models.ForeignKey(Client)
    consultant = models.ForeignKey(Consultant)
    dateFinMission = models.DateTimeField("date de fin de mission")
    def __str__(self):
        return self.poste + "  " + self.client + "   " + dateDebutMission + "   " + dateFinMission

class Mission_en_cours(models.Model):
    dateDebutMission = models.DateTimeField("date de debut de mission")
    poste = models.CharField(max_length=200)
    client = models.ForeignKey(Client)
    consultant = models.ForeignKey(Consultant)
    def __str__(self):
        return self.consultant.nom + "   " + self.consultant.prenom + "  " + \
        self.poste + "  (client : " + "   " + self.client.societe  + "   " + \
        self.client.nom + " " + self.client.prenom + " )"


class Activite(models.Model):
    actitivite = {}
    actitivite_saisie_par_consultant = False
    activite_validee_par_client = False
    consultant = models.ForeignKey(Consultant)
