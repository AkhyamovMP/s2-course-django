from msilib.schema import ListView
from unittest import result
from django.shortcuts import render, redirect
from .models import Articles, Certificates, Users
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

    articles = Articles.objects.all()[::-4]
    #print(articles[0].author)

    data = {
        'title': 'ЯДокументы',
        'articles': articles
        
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
        search_request = request.POST['search_request']
    certificates_list = Certificates.objects.all()
    search_list = []

    # change accuracy if need more wide but less accurate search
    def search_by_symbol(target_word, word, acc=0.8, shift_check=3, shift_cost=0.5, prize=0.25):
        target_word_list = [x for x in target_word.lower()]
        word_list = [x for x in word.lower()]
        accuracy = 1
        min_len = min(len(word_list), len(target_word_list))
        shift = 0
        for n in range(min_len-1):
            if word_list[n+shift] != target_word_list[n]:
                if n+shift < min_len-1:
                    if n+shift_check <= min_len-1:
                        allowed_check = shift_check
                    else:
                        allowed_check = min_len-1-n
                    if word[n+shift+1:n+shift+1+allowed_check] == target_word[n:n+allowed_check]:
                        shift += 1
                        accuracy -= 1 / min_len * shift_cost
                    elif word[n+shift:n+shift+allowed_check] == target_word[n+1:n+1+allowed_check]:
                        shift -= 1
                        accuracy -= 1 / min_len * shift_cost
                    else:
                        accuracy -= 1 / min_len
            else:
                accuracy += prize * 0.01
            if accuracy < acc:
                return False
        return (word, accuracy)

        '''
    
    def search_by_word(target_phrase, phrase, acc=0.8, shift_check=1, shift_cost=0.5):
        target_phrase_list = target_phrase.split()
        phrase_list = phrase.split()


        def group_items(lst, n):
            return [lst[i:i + n] for i in range(0, len(lst), n)]

        
        res = group_items(phrase_list, (len(target_phrase_list) + shift_check * 2))
        accuracy = []


        for n in res:
            phrase_joined = ' '.join(n) 
            if len(phrase_joined) >= len(target_phrase):
                ln = len(phrase_joined) - len(target_phrase) - 1
                max_acc = float(0.0)              
                for y in range(ln):
                    phrase_acc = search_by_symbol(target_phrase, phrase_joined[y:len(phrase_joined)-1])
                    if phrase_acc:
                        print(phrase_acc)
                        if phrase_acc[1] > max_acc:
                            max_acc = phrase_joined
                n.append(max_acc)

        print(res)






        return target_phrase_list

    print(search_by_word('прикол', 'когда нибудь здесь будет номральная фраза приколы существуют что касается приколов я их ем'))
        '''

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


'''



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
