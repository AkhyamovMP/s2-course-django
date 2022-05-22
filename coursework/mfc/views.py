from django.shortcuts import render

def loginpage(request):
    return render(request, 'mfc/index.html')

def homepage(request):
    return render(request, 'mfc/home.html')

    