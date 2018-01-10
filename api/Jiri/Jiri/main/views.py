from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def login_view(request):
    errors = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    errors.append('Le nom d\'utilisateur et/ou le mot de passe est incorrect.')
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form, 'errors': errors})