from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'account/index.html')

def sign_up(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.changed_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('account:index')
    form=SignUpForm()        
    return render(request, 'account/sign_up.html', context={'form': form})
    