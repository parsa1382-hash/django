from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
"""
def index(request):
    qlist = Question.objects.all()
    output = ", ".join([q.qtext for q in qlist])
    return HttpResponse(output)


def index(request):
    return HttpResponse("hello world")


def index(request):
    return render(request, ‘index.html’)
"""

def index(request):
    #a = "templates/index.html"
    return render(request, 'zavie/index.html')

def news(request):
    return render(request, 'zavie/news.html')

# Create your views here.
