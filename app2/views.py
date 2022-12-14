from http.client import HTTPResponse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from app2.forms import FileForm
from .models import App2

class App2UpdateView(UpdateView):
    model = App2
    form_class = FileForm
    success_url = '/app2'
    template_name = "app2/upload_file.html"

class App2CreateView(CreateView):
    model = App2
    form_class = FileForm
    success_url = '/app2'
    template_name = "app2/upload_file.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class App2DeleteView(DeleteView):
    model = App2
    context_object_name = 'file'
    success_url = '/app2'
    template_name = "app2/delete.html"

class App2ListView(LoginRequiredMixin, ListView):
    model = App2
    context_object_name = 'files'
    template_name="app2/list_files.html"
    login_url = 'login'

    def get_queryset(self):
        return self.request.user.files.all()

class App2DetailView(DetailView):
    model = App2
    context_object_name = 'file'
    template_name="app2/file.html"


""" # Create your views here.
def list_files(request):
    all_item = App2.objects.all()
    return render(request, 'app2/list_files.html', {'files': all_item}) """

""" def detail(request, pk):
    try: 
        item = App2.objects.get(pk=pk)
    except App2.DoesNotExist:
        raise Http404("The file does not exist.")
    return render(request, 'app2/file.html', {'file': item}) """

    
