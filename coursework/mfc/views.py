from turtle import title
from django.shortcuts import render, redirect
from .models import Application, Articles, Certificates, Departments, Users, Passports
from .forms import PassportForm, UserLoginForm, UserRegForm, ArticleForm, ApplicationForm
from django.contrib.auth import login, logout


def sign_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    data = {
        'title': 'ЯДокументы',
        'form': form,
    }
    return render(request, 'registration/login.html', data)


def sign_up(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            app = form.save()
            new_user = Users.objects.create(user=app)
            return redirect('sign-in')
    else:
        form = UserRegForm()
    data = {
        'title': 'ЯДокументы',
        "form": form
    }
    return render(request, 'registration/registration.html', data)


def user_logout(request):
    logout(request)
    return redirect('home')


def homepage(request):
    articles = Articles.objects.all()
    data = {
        'title': 'ЯДокументы',
        'articles': articles
    }
    return render(request, 'home.html', data)


def article(request, article_id):
    article = Articles.objects.get(pk=article_id)
    data = {
        'title': 'ЯДокументы',
        'article': article
    }
    return render(request, 'article.html', data)


def edit_article(request):
    form = ArticleForm()
    data = {
        'title': 'ЯДокументы',
        'form': form
    }
    return render(request, 'edit-article.html', data)


def certificates(request):
    data = {
        'title': 'ЯДокументы',
        'certificatesList': Certificates.objects.all()
    }
    return render(request, 'certificates.html', data)


def add_certificate(request, certificate_id):
    if not request.user.is_authenticated:
        return redirect('sign-in')
    certificate = Certificates.objects.get(pk=certificate_id)
    departments = Departments.objects.all()
    form = ApplicationForm()
    if request.method == 'POST':
        app = form.save(commit=False)
        app.certificate = certificate
        app.department = Departments.objects.get(pk=request.POST['department'])
        app.user = Users.objects.get(pk=request.user.id)
        app.save()
    data = {
        'title': 'ЯДокументы',
        'certificate': certificate,
        'departments': departments,
        'form': form
    }
    return render(request, 'add-certificate.html', data)


def add_passport(request):
    if not request.user.is_authenticated:
        return redirect('sign-in')
    if not Users.objects.get(pk=request.user.id).passport_id:
        if request.method == 'POST':
            form = PassportForm(request.POST)
            if form.is_valid():
                m = form.save()
                user = Users.objects.get(pk=request.user.id)
                user.passport_id = m
                user.save()
                return redirect('show-passport')
    else:
        return redirect('show-passport')
    data = {
        'form': PassportForm(),
        'title': 'ЯДокументы',
    }

    return render(request, 'add-passport.html', data)


def show_passport(request):
    if not request.user.is_authenticated:
        return redirect('sign-in')
    data = {
        'title': 'ЯДокументы',
        'passport': Users.objects.get(pk=request.user.id).passport_id
    }
    return render(request, 'show-passport.html', data)


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

    # add some more lists to search in

    search_result = []
    for word in search_list:
        res = search_by_symbol(search_request, word[0])
        if res:
            search_result.append(
                {'title': word[0], 'url': word[1], 'id': word[2], 'accuracy': res[1]})

    data = {
        'title': 'ЯДокументы',
        'search_request': search_request,
        'search_result': sorted(search_result, key=lambda x: x['accuracy'], reverse=True)
    }
    return render(request, 'search.html', data)
