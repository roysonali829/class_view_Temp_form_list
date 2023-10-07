from typing import Any
from django.shortcuts import render

from django.views.generic import TemplateView,FormView,ListView
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

class student_insert_form(FormView):
    form_class = StudentForm
    template_name = 'student_insert_form.html'
    
    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return HttpResponse('data inserted')

class display_student(ListView):
    model = Student
    template_name = 'display_student.html'
    context_object_name = 'stlist'
    ordering = ['Sage']