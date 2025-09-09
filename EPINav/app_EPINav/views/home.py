from django.shortcuts import render
from app_EPINav.views.decorators import login_required_custom

@login_required_custom
def home(request):
    return render(request, 'app_EPINav/pages/home.html')
