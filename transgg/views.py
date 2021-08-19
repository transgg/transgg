from django.http import HttpResponse

from django.views.generic import TemplateView
from .models import Category, Question

class StyledTemplateView(TemplateView):
    pass