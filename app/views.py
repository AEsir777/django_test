from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_request(request):
    return render(request, 'app/index.html', 
    {'content': 'This is the content passed from view to the template.'})
# {} pass the information from the view to the template

@login_required(login_url='/admin')
def authorize(request):
    return render(request, 'app/authorized.html', {'authorize': 'This is the authorized content.'})
