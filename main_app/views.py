from django.shortcuts import render
from .models import lists
from django.views.generic.edit import CreateView, DeleteView

def index(request):
    Lists = lists.objects.all()
    return render(request, 'index.html',{'lists': lists})


class listsCreate(CreateView):
    model = lists
    fields = '__all__'
    
   
def delete(request, lists_id):
    lists_id.objects.filter(id=lists_id).delete()
    return ('index')   