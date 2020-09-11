from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    qlist = Question.objects.all()
    output = ", ".join([q.qtext for q in qlist])
    return HttpResponse(output)

"""
def index(request):
    return HttpResponse("hello world")
"""



# Create your views here.
