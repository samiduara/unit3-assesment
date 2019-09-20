from django.shortcuts import render
from .models import lists
from django.views.generic.edit import CreateView, DeleteView

def index(request):
    Lists = lists.objects.all()
    return render(request, 'index.html',{'lists': lists})


class listsCreate(CreateView):
    model = lists
    fields = '__all__'
    

class listsDelete(DeleteView):
    model = lists
   