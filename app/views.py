from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ModalOneView(TemplateView):
    template_name = "modal_one_view.html"
