from django.shortcuts import render, redirect

from django.http import HttpResponse


def fb(request):
    return render(request,'seaform.html')

def home(request):
    return render(request,'facebook.html')
