from django.shortcuts import render
from django.template import loader
from django.contrib.auth import authenticate, login



# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import ConsultantForm






def index(request):
    if request.user.is_authenticated():
        template = loader.get_template('cra/index.html')
        consultant_liste = Consultant.objects.filter(pk=request.user.pk)[0:]
        commercial_liste = Commercial.objects.filter(pk=request.user.pk)[0:]
        commercial_liste2 = Commercial2.objects.filter(pk=request.user.pk)[0:]
        if consultant_liste :
            consultant = Consultant.objects.filter(pk=request.user.pk)[0]
        else :
            consultant=None
        if commercial_liste :
            commercial = Commercial.objects.filter(pk=request.user.pk)[0]
            print(commercial.liste_consultants)
        else:
            commercial = None

        if commercial_liste2 :
            commercial2 = Commercial2.objects.filter(pk=request.user.pk)[0]
            print(commercial.liste_consultants)
        else:
            commercial = None
        latest_consultants_list = Consultant.objects.order_by('-date_embauche')[:5]
        context = {
            'latest_consultants_list':latest_consultants_list,'user':request.user,'commercial':commercial,'commercial2':commercial2,'consultant':consultant,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("/login")

def index2(request):
    consultant = consultant.objects.get(pk=1)
    form = ConsultantForm(request.POST, instance=consultant)
    return HttpResponse(template.render(context, request))

    article = Article.objects.get(pk=1)

def login2(request):
    consultantForm = ConsultantForm(request.POST)
    template = loader.get_template('cra/login.html')
    context = {
        'formset':consultantForm,
    }
    return HttpResponse(template.render(context, request))

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            print("authentification ok")
        else:
            # Return a 'disabled account' error message
            print("compte desactive")
    else:
        # Return an 'invalid login' error message.
        print("mot de passe incorrect")


def register(request):
    return HttpResponse("Page to register")
