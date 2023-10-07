from typing import Any
from django.shortcuts import render

from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse

# Create your views here.

class temp(TemplateView):
    template_name = 'temp.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ECDO = super().get_context_data(**kwargs)
        # ECDO['name'] = 'bristi'
        ECDO['SFO'] = StudentForm()
        return ECDO
    
    def post(self,request):
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data inserted')