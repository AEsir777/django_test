import datetime
from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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