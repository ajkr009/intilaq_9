from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

# 1. ഹോം പേജ് വ്യൂ
def home(request):
    context = {
        'portal_name': 'Welcome to Student Hub',
        'welcome_msg': 'Manage your academic dashboard here.',
        'announcements': [
            'Internal exams will start on Monday.',
            'Library books should be returned before Friday.',
            'Python workshop registration is now open.'
        ]
    }
    return render(request, 'home.html', context)

# 2. എബൗട്ട് പേജ് വ്യൂ
def about(request):
    return render(request, 'about.html')

# 3. രജിസ്ട്രേഷൻ വ്യൂ
def register(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('password')
        cp = request.POST.get('confirm_password')

        if p != cp:
            messages.error(request, "Passwords do not match!")
            return render(request, 'register.html')

        if User.objects.filter(username=u).exists():
            messages.error(request, "Username already taken!")
            return render(request, 'register.html')

        # പുതിയ യൂസറെ ഉണ്ടാക്കുന്നു
        user = User.objects.create_user(username=u, email=e, password=p)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'register.html')

# 4. ലോഗിൻ വ്യൂ
def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password!")
            return render(request, 'login.html')

    return render(request, 'login.html')

def fun_page(request):
    return render(request, 'fun.html')

#5. ലോഗ് ഔട്ട് വ്യൂ
def logout_view(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')