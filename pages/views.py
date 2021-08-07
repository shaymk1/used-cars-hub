from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
  # return HttpResponse('yebo yes')
  return render(request, 'pages/home.html')
