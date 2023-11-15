from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kane(request):
    return render(request,'kane.html')


def warner(request):
    return HttpResponse("<h1>warner</h1>")