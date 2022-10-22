from django.shortcuts import render
from .models import App2

# Create your views here.
def list_files(request):
    all_item = App2.objects.all()
    return render(request, 'app2/list_files.html', {'files': all_item})



    
