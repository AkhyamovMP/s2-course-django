from msilib.schema import ListView
from unittest import result
from django.shortcuts import render, redirect
from .models import Articles, Certificates, Users
from .forms import UserForm, ArticleForm


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

    def checkNewUsername(newUsername, users):
        for user in users:
            if newUsername == user.username:
                return 1
        return 0
    return render(request, 'mfc/index.html', data)


def homepage(request):

    articles = Articles.objects.all()
    print(articles[2])

    data = {
        'title': 'ЯДокументы',
        'articles': articles

    }
    return render(request, 'mfc/home.html', data)


def article(request, article_id):
    article = Articles.objects.get(pk=article_id)
    data = {
        'title': 'ЯДокументы',
        'article': article
    }

    return render(request, 'mfc/article.html', data)


def certificates(request):

    data = {
        'title': 'ЯДокументы',
        'certificatesList': Certificates.objects.all()
    }

    return render(request, 'mfc/certificates.html', data)


def show_certificate(request, certificate_id):
    certificate = Certificates.objects.get(pk=certificate_id)

    data = {
        'title': 'ЯДокументы',
        'certificate': certificate
    }

    return render(request, 'mfc/show-certificate.html', data)


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
        search_list.append(
            (certificate.name, 'show-certificate', str(certificate.certificate_id)))

    #add some more lists to search in

    search_result = []
    for word in search_list:
        res = search_by_symbol(search_request, word[0])
        if res:
            search_result.append({'title': word[0], 'url': word[1], 'id': word[2], 'accuracy': res[1]})

    print(result)

    data = {
        'title': 'ЯДокументы',
        'search_request': search_request,
        'search_result': sorted(search_result, key=lambda x: x['accuracy'], reverse=True)
    }
    return render(request, 'mfc/search.html', data)


def edit_article(request):

    form = ArticleForm()

    data = {
        'title': 'ЯДокументы',
        'form': form
    }

    return render(request, 'mfc/edit-article.html', data)
