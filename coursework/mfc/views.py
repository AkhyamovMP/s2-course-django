from django.shortcuts import render
from .models import Certificates


def loginpage(request):
    return render(request, 'mfc/index.html')


def homepage(request):
    return render(request, 'mfc/home.html', {'title': 'ЯДокументы'})


def certificates(request):
    certificatesList = Certificates.objects.all()
    return render(request, 'mfc/certificates.html', {'title': 'ЯДокументы', 'certificatesList': certificatesList})
