from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail

from .forms import ContactForm

import random

from .models import HomePage, About
from galery.models import Photo

class HomeView(TemplateView):
    template_name = 'index.html'

    extra_context = {
        "photos": Photo.objects.filter(frontpage = True)
    }

    homepage_contact = HomePage.objects.all()

    if homepage_contact:
        extra_context["title"] = homepage_contact[0].title
        extra_context["subtitle"] = homepage_contact[0].subtitle
        extra_context["content"] = homepage_contact[0].contect

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = "/contact/sent/"

    extra_context = {
        "title" : "Kérjen tőlünk ajánlatot"
    }

    def form_valid(self, form):

        send_mail(
            "Contact",
            form.data["message"],
            form.data["email"],
            ["balazs21mate@gmail.com"],
            fail_silently=False
        )

        return super().form_valid(form)

class ContactSentView(TemplateView):
    template_name = "email_sent.html"

class AboutView(TemplateView):
    template_name = 'about.html'

    photos = Photo.objects.all()

    extra_context = {
        "photo": random.choice(photos)
    }

    about_contact = About.objects.all()

    if about_contact:
        extra_context["title"] = about_contact[0].title
        extra_context["content"] = about_contact[0].content