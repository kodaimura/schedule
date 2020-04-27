from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, LogInForm
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class Login(LoginView):
    form_class = LogInForm
    template_name = 'accounts/login.html'
    
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/login.html'
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('schedule')
            
    else:
        form = SignUpForm()
        
    return render(request, 'accounts/signup.html',{'form': form })
    
    
