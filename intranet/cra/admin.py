from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Employe,Consultant,Client,Mission_terminee,Mission_en_cours,Activite

admin.site.register(Employe)
admin.site.register(Consultant)
admin.site.register(Mission_terminee)
admin.site.register(Client)
admin.site.register(Mission_en_cours)
admin.site.register(Activite)
