from django.shortcuts import render

def home(request):
    return render(request, 'app_EPINav/pages/home.html')

