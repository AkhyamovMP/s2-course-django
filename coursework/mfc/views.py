from msilib.schema import ListView
from unittest import result
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
    data = {
        'title': 'ЯДокументы',
    }
    return render(request, 'mfc/home.html', data)


def certificates(request):

    data = {
        'title': 'ЯДокументы',
        'certificatesList': Certificates.objects.all()
    }

    return render(request, 'mfc/certificates.html', data)


def search(request):
    if request.method == 'POST':
        # print(request.POST)
        search_request = request.POST['search_request']
        #search_result = Certificates.objects.filter(name__contains=search_request)
    certificates_list = Certificates.objects.all()
    search_list = []

    # change accuracy if need more wide but less accurate search
    '''
    def search_by_symbol(target_word, list, acc=0.8):
        target_word_list = [x for x in target_word.lower()]
        result = []
        for word in list:
            accuracy = 1
            word_list = [x for x in word.lower()]
            min_len = (min(word_list, target_word_list))
            for n in range(min_len-1):
                if word_list[n] != target_word_list[n]:
                    accuracy -= 1 / min_len
                if accuracy < acc:
                    break
            if accuracy >= acc:
                result.append((word, accuracy))
        return result
'''

    def search_by_symbol(target_word, word, acc=0.8, shift_check=3, shift_cost=0.5):
        target_word_list = [x for x in target_word.lower()]
        word_list = [x for x in word.lower()]
        accuracy = 1
        min_len = min(len(word_list), len(target_word_list))
        shift = 0
        for n in range(min_len-1):
            if word_list[n+shift] != target_word_list[n]:
                if n+shift_check <= min_len-1:
                    if word[n+1:n+1+shift_check] == target_word[n:n+shift_check] and n != 0:
                        shift += 1
                        accuracy -= 1 / min_len * shift_cost
                        continue
                    elif word[n:n+shift_check] in target_word[n+1:n+1+shift_check]:
                        shift -= 1
                        accuracy -= 1 / min_len
                        continue
                    else:
                        accuracy -= 1 / min_len
            if accuracy < acc:
                return False
        return (word, accuracy)

    for certificate in certificates_list:
        search_list.append(certificate.name)

    search_result = []
    for word in search_list:
        res = search_by_symbol(search_request, word)
        if res:
            search_result.append(res)

    print(result)

    data = {
        'title': 'ЯДокументы',
        'search_request': search_request,
        'search_result': search_result
    }
    return render(request, 'mfc/search.html', data)


'''

class Search(ListView):
    model = Users()
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Users.objects.filter(number__icontains=query)

        return object_list


result = first_string.rfind()
def search(request):
    print('aboba')

    return redirect('certificates')

# cities/views.py
class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'
    queryset = City.objects.filter(name__icontains='Boston') # новый
    '''
