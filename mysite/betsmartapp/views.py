from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomLoginForm
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from .models import Plan
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def login_user(request):
    form = CustomLoginForm()
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
        else:
            print(form.errors)

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            print(f"Usuário criado: {user.username}") 
            
            login(request, user)
            return redirect('start')  
    else:
        form = RegisterForm()
    
    return render(request, 'registo.html', {'form': form})

def start(request):
    # Aqui você pode recuperar todos os planos para exibi-los
    plans = Plan.objects.all()
    return render(request, 'get_start.html', {'plans': plans})


@login_required
def choose_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    user_profile = request.user.profile
    user_profile.plan = plan
    user_profile.save()
    return redirect('planfree.html')
    
    

def profile_view(request):
    # Get the user's profile (assuming you have a Profile model linked via OneToOneField)
    profile = request.user.profile  # Will automatically use the signal-created profile
    
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)

def logout(request):
    auth_logout(request)
    return redirect('home')

def plan_free(request):
    if not request.user.profile.plan:
        return redirect('get_start.html')
    return render(request, 'planfree.html')