from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from content.models import contact, slider
from multimedia.models import gallery


class Gallery (TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super(Gallery, self).get_context_data(**kwargs)
        context['gallery'] = gallery.objects.published()
        context['contacto'] = contact.objects.first()
        context['slider'] = slider.objects.first()
        print(gallery.objects.get(id=5).categoria)
        return context
