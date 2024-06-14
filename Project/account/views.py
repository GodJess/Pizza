from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import auth
from django.conf import settings
from .models import User
from django.shortcuts import get_object_or_404

# Create your views here.
def account(request):
    ak = request.session.get(settings.USER_SESSION_ID,{})
    context={
        'ak': ak,
    }
    return render(request, 'account/account.html', context)

def snake(request):
    return render(request, 'account/snake.html')

def tetris(request):
    return render(request, 'account/tetris.html')

def avtoriz(request):
   error = ""
   name = request.POST.get('login')
   password = request.POST.get('password')
   model = User.objects.filter(login=name, password = password)
   ak = request.session.get(settings.USER_SESSION_ID, {})
   if  model.exists():
        for key in list(ak.keys()):
            del ak[key]
       
       # Удаляем пользователя из сессии, если он уже там присутствует, 
        if name in ak:
           del ak[name]
           
        user = model.first()
       # Добавляем нового пользователя в сессию
        ak[name] = {"login": name, "password": password, 'mail': user.mail, 'id': user.id}   
        request.session[settings.USER_SESSION_ID] = ak
       
        return redirect('account')
   else:
       error = ''

   context = {'error': error}  
    
   return render(request, 'account/avtoriz.html', context)

           

def register(request):
    error = ""
    errors = ""
    repassword = request.POST.get('repassword')
    password = request.POST.get('password')
    if request.method == "POST":
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            if repassword == password:
                forms.save()
                return redirect('avtoriz')
            else: 
                errors = "Пароли не совпадают"
        else:
            error = "Форма была не верной"
            
    form = UserRegisterForm()
    context={
        "form": form,
        "error": error,
        "errors": errors
    }
    return render(request, 'account/register.html', context)

def personal_data(request):
    ak = request.session.get(settings.USER_SESSION_ID, {})
    data = request.session.get(settings.USER_SESSION_DATA, {})
    length = len(data)
    login_ak = ak.get('login')
    login_data = data.get("login")
    #data = User.objects.get(login = login)
    context = {
        "ak": ak,
        'data': data,
        'length': length,
    }
    return render(request, 'account/persdata.html', context)

def add_name(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    ak = request.session.get(settings.USER_SESSION_ID, {})
    data = request.session.get(settings.USER_SESSION_DATA, {})
    login = ak.get('login')
    data[login]= {"name": name, "surname": surname, 'login': login, }
    request.session[settings.USER_SESSION_DATA] = data
    
    return redirect('persdata')