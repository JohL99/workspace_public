from django.urls import path

from . import views

urlpatterns = [
    path('', forms.ContactForm, name='ContactForm'),
]
