from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('', views.index, name="views"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name='about')


]
