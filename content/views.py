from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from content.models import Service, contact


class ServicesDetail(DetailView):
    context_object_name = 'service'
    model = Service
    template_name = "service.html"

    def get_context_data(self, **kwargs):
        # Item_list=self.object.get_Items()
        # paginator = Paginator(Item_list, 10)
        # page = self.request.GET.get('page')
        # try:
        #     Items = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     Items = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     Items = paginator.page(paginator.num_pages)

        context = super(ServicesDetail, self).get_context_data(**kwargs)
        context['contacto'] = contact.objects.first()

        # context['Items'] = Items
        return context

