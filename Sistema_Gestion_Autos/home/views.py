from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from user.forms import UserRegisterForm  

class LoginView(View):
    def get(self, request):
        return render(
            request,
            'index/login.html'  
        )
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user:
                login(request, user)
                return redirect('index')  # Redirige a la vista index después del login
        return redirect('login')  # Redirige al login en caso de fallo

class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'index/register.html'  

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form
            }  
        )
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loguea automáticamente al usuario registrado
            return redirect('index')  # Redirige a la vista index después del registro
        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )

class LogoutView(View):
    def get(self, request):
        logout(request)  # Cierra la sesión del usuario
        return redirect('login')  # Redirige al login después de cerrar sesión

@login_required(login_url="/login/")
def index_view(request):
    return render(
        request,
        'index/index.html'  
    )
