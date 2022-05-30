from django.shortcuts import render, redirect
from .models import Certificates, Users
from .forms import UserForm


def loginpage(request):

    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if form.data['form-type'] == 'login':
                allUsers = Users.objects.all()
                for user in allUsers:
                    if form.data['username'].lower() == user.username.lower() and form.data['password'] == user.password:
                        return redirect('home')
            elif form.data['form-type'] == 'registration':
                print(form.data)
                #form.save()
                #return redirect('home')

        else:
            error = 'Ошибка в заполнении формы'

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'mfc/index.html', data)


def homepage(request):
    return render(request, 'mfc/home.html', {'title': 'ЯДокументы'})


def certificates(request):

    data = {
        'title': 'ЯДокументы',
        'certificatesList': Certificates.objects.all()
    }

    return render(request, 'mfc/certificates.html', data)
