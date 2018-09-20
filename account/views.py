from django.shortcuts import render,redirect
from .forms import SignUpForm, SignInForm
from .models import Account
# from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    return render(request,'account/index.html')

def sign_up(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username = cd['username']
            email = cd['email']
            password = cd['password1']
            user=Account.objects.create_user(username=username,email=email,password=password)
            return redirect(reverse('account:sign_in'))
        else:
            return render(request, 'account/sign_up.html', context={'form': form})
    form=SignUpForm()        
    return render(request, 'account/sign_up.html', context={'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('account:index'))

            else:
                return HttpResponse('no such user')
    form = SignInForm()
    return render(request,'account/sign_in.html',context={'form':form})