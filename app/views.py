import datetime
from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'app/register.html'
    success_url = 'app2'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('file.list')
        return super().get(request, *args, **kwargs)

class AppLogoutView(LogoutView):
    template_name = 'app/logout.html'

class AppLoginView(LoginView):
    template_name = 'app/login.html'

class AppView(TemplateView):
    template_name = 'app/index.html'
    extra_context = {'today': datetime.time(),
                     'content': 'This is the content passed from view to the template.'}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'app/authorized.html'
    extra_context = {'authorize': 'This is the authorized content.'}
    login_url = '/admin'

""" @login_required(login_url='/admin')
def authorize(request):
    return render(request, 'app/authorized.html', {})
# {} pass the information from the view to the template """