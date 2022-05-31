from django.shortcuts import render, redirect
from .models import Certificates, Users
from .forms import UserForm


def loginpage(request):

    error = ''
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if form.data['form-type'] == 'login':
                allUsers = Users.objects.all()
                print(form.data)
                for user in allUsers:
                    if form.data['username'] == user.username and form.data['password'] == user.password:
                        return redirect('home')
                    elif form.data['username'] == user.username and form.data['password'] != user.password or form.data['username'] != user.username and form.data['password'] == user.password:
                        error = 'Неверный логин или пароль'
                        break

            elif form.data['form-type'] == 'registration':
                if not checkNewUsername(form.data['newUsername'], Users.objects.all()):
                    if form.data['newPassword'] == form.data['newPasswordConf']:
                        newUser = Users()
                        newUser.username = form.data['newUsername']
                        newUser.password = form.data['newPasswordConf']
                        newUser.save()
                        return redirect('home')
                    else:
                        error = 'Введённые пароли не совпадают'
                else:
                    error = 'Пользователь с таким именем уже существует'
        else:
            error = 'Ошибка в заполнении формы'

    data = {
        'form': form,
        'formError': error
    }

    return render(request, 'mfc/index.html', data)


def checkNewUsername(newUsername, users):
    for user in users:
        if newUsername == user.username:
            return 1
    return 0


def homepage(request):
    return render(request, 'mfc/home.html', {'title': 'ЯДокументы'})


def certificates(request):

    data = {
        'title': 'ЯДокументы',
        'certificatesList': Certificates.objects.all()
    }

    return render(request, 'mfc/certificates.html', data)
