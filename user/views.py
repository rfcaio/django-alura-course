from django.contrib.auth.models import User
from django.shortcuts import redirect, render

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if (not username.strip()):
            print('A valid user name is required.')
            return redirect('signup')

        if (password != confirm_password):
            print('The two passwords are not equals.')
            return redirect('signup')

        if (User.objects.filter(email=email).exists()):
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
