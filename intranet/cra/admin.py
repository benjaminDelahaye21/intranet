from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Employe,Consultant

admin.site.register(Employe)
admin.site.register(Consultant)
admin.site.register(Mission)
admin.site.register(Client)

