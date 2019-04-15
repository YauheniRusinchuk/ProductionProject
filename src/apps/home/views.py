from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home/index.html', {})


class LoginView(View):
    ''' Отображение страницы входа  '''
    def get(sefl, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home_page')
        return render(request, 'home/login.html', {})

    ''' Метод пост для проверки существования юзера и вход '''
    def post(sefl, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home_page')
        else:
            return redirect('home:login_page')
