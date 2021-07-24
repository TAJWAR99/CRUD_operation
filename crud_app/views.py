from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUser,UpdateForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

#home page
def home(request):
    users = User.objects.all()[1:]
    return render(request,'index.html',{'users':users})

 #login
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('user')
        else:
            messages.info(request,"username or email or password didn't match")

    return render(request,'login.html')

#logout
def logoutPage(request):
    logout(request)
    return redirect('/')

#registration
def register(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Congratulations! Account was created for "{username}".')
            return redirect('user')

        else:
            messages.info(request,'Username or Email already exists')
    context = {'form':form}
    return render(request,'register.html',context)

#user info
@login_required(login_url='home')
def user(request):
    users = User.objects.all()[1:]
    return render(request,'user.html',{'users':users})

#update user
@login_required(login_url='home')
def updateUser(request,pk):
    user = User.objects.get(id=pk)
    form = UpdateForm(instance=user)
    if request.method == 'POST':
        form = UpdateForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account was updated for "{username}".')
            return redirect('user')
    context = {'form':form}
    return render(request,'update.html',context)

#delete user
@login_required(login_url='home')
def deleteUser(request,pk):
    user = User.objects.get(id=pk)
    ad = User.objects.get(id=1)

    owner = request.POST.get('user1')
    pass1 = request.POST.get('pass1')

    admin = request.POST.get('user2')
    pass2 = request.POST.get('pass2')

    
    if request.method == "POST":
        #Confirming if the info was given in the correct allocated place
        if user.username == owner and ad.username == admin:
            check1 = authenticate(request,username=owner,password=pass1) #for account owner
            check2 = authenticate(request,username=admin,password=pass2) #for admin
            if check1 is not None and check2 is not None:
                user.delete()
                messages.success(request,f'An account was deleted.')
                return redirect('user')
            elif check1 is None:
                messages.info(request,'Wrong Owner username or password!!!Please enter the correct one')
            elif check2 is None:
                messages.info(request,'Wrong admin username or password!!!Please enter the correct one')
        else:
            messages.info(request,'Wrong info given!!!Please enter the info in the allocated place')

    return render(request,'delete.html',{'user':user})