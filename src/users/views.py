from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy
from django.views.generic import FormView, DetailView, UpdateView
from django.views.generic.edit import UpdateView
from .forms import RegisterForm, ProfileForm
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.models import Group
from django.contrib.auth import login

User = get_user_model()

class Login(LoginView):
    template_name = 'users/login.html'


class Logout(LogoutView):
    next_page = '/'


class RegistrationView(FormView):
    template_name = 'users/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('books:main')

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        username = data['username']
        password = data['password2']
        phone_number = data['phone_number']
        email = data['email']
        customer_group = Group.objects.get(name='customer')
        user = User.objects.create_user(username, email, password,)
        user.groups.add(customer_group.pk)
        user.save()
        login(self.request, user)
        user_profile = Profile.objects.create(user=user, phonenumber=phone_number)        
        return super().form_valid(form)


class ProfileView(DetailView):
    model = Profile
    template_name = 'users/profile.html'


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm