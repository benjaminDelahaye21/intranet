from django.shortcuts import render
from django.contrib.auth import authenticate
from django.template import loader
from django.contrib.auth import authenticate, login



# Create your views here.
from django.http import HttpResponse
from .models import Consultant


def index(request):
    latest_consultants_list = Consultant.objects.order_by('-date_embauche')[:5]
    template = loader.get_template('cra/index.html')
    context = {
        'latest_consultants_list': latest_consultants_list,
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
