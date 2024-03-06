import hashlib
from django.db.utils import IntegrityError
from django.shortcuts import render
from django.views import View
from project_users.models import CustomUser


# Create your views here.

class HomePageView(View):
    TITLE = "Home Page"

    def get(self, request, *args, **kwargs):
        count = CustomUser.objects.count()
        data = CustomUser.objects.filter(pk__gte=count - 10)
        new_data = []
        for user in data:
            before_at, after_at = user.email.split('@')
            hidden_part = '*' * (len(before_at) - 2)
            new_data.append(f'{before_at[:2:]}{hidden_part}@{after_at}')
        return render(request, 'home_page.html', context={'users': new_data, 'count': count, 'title': self.TITLE})


class LoginPageView(View):
    TITLE = "Login Page"

    def get(self, request, *args, **kwargs):
        return render(request, 'sing_in.html', context={'title': self.TITLE})

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = hashlib.md5(request.POST.get('password').encode()).hexdigest()
        data = CustomUser.objects.filter(email=email)
        try:
            if data[0].email and password == data[0].pass_hash:
                message = f'Welcome back, {data[0].email}'
            else:
                message = 'Check your email and password to try again'
        except IndexError:
            message = 'Check your email and password to try again'
        return render(request, 'sing_in.html', context={'title': self.TITLE, 'message': message})


class RegistrationPageView(View):
    TITLE = "Registration Page"

    def get(self, request):
        return render(request, 'sing_up.html', context={'title': self.TITLE})

    def post(self, request):
        email = request.POST.get('email')
        password = hashlib.md5(request.POST.get('password').encode()).hexdigest()
        confirm_password = hashlib.md5(request.POST.get('confirm_password').encode()).hexdigest()
        try:
            first, second = email.split('@')
            before_dot, after_dot = second.split('.')
        except ValueError:
            email = ''
        print(email, password, confirm_password)
        is_exist = True if email and password and confirm_password else False
        try:
            if is_exist and password == confirm_password:
                user = CustomUser(email=email, pass_hash=password)
                user.save()
                message = 'registration is OK. Please login or register a new'
            elif email and password != confirm_password:
                message = 'passwords do not match'
            else:
                message = 'please type email, password and confirm_password'
        except IntegrityError:
            message = 'This email does exist. Please login or register a new'
        return render(request, 'sing_up.html', context={'title': self.TITLE, 'message': message})
