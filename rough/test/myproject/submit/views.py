from myapp.forms import ContactForm
from django.views.generic.edit import FormView

def ContactForm(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'
