from django.shortcuts import render
from . forms import TestForm
# Create your views here.

def django_form(request):
    form = TestForm()
    return render(request, 'django_form.html', {'form' : form})

