from django.conf.urls import url


from . import views

urlpatterns = [
   url(r'^login2$', views.login, name='login2'),
   url(r'^register$', views.register, name='register'),
   url(r'^$', views.my_view, name='my_view'),
   url(r'^index$', views.index, name='index'),
   ]
