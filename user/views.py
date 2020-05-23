from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'dashboard.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email == '' or password == '':
            print('A valid email and password are required.')
            return redirect('signin')

        if User.objects.filter(email=email).exists():
            username = (
                User.objects
                    .filter(email=email)
                    .values_list('username', flat=True)
                    .get()
            )
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not username.strip():
            print('A valid user name is required.')
            return redirect('signup')

        if password != confirm_password:
            print('The two passwords are not equals.')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            print('A user with email %s already exists.' % email)
            return redirect('signup')

        user = User.objects.create_user(
            email=email,
            password=password,
            username=username
        )
        user.save()
        print('User created.')
        return redirect('index')
    return render(request, 'signup.html')
