from django.shortcuts import render
from django.views.generic import DetailView
from .models import Kitchen, Sofa, Lamp


def index(request):
    return render(request, 'index.html', {})


class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'kitchens': Kitchen,
        'sofas': Sofa,
        'lamps': Lamp
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'