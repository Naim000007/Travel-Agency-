from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']
        username = request.POST[ 'username']
        password1 = request.POST[ 'password1']
        password2 = request.POST['password2']
        email = request.POST[ 'email']

        user = User.objects.create(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print("User created")
        return redirect('/')


    else:
        return render(request, 'register.html')

 