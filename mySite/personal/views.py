from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import RegistrationForm
from django.shortcuts import render
from .models import Post

def about(request):
    return render(request, 'personal/about.html')

def portfolio(request):
    return render(request, 'personal/portfolio.html')

def contact(request):
    return render(request, 'personal/contact.html')

def blog_post_list(request):
    posts = Post.objects.all()
    return render(request, 'personal/blog_post_list.html', {'posts': posts})

def blog_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'personal/blog_post_detail.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal:login')
    else:
        form = RegistrationForm()
    return render(request, 'personal/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'personal/home.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('personal:home')
    else:
        form = AuthenticationForm()
    return render(request, 'personal/login.html', {'form': form})
