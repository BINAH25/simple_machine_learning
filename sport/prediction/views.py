from django.shortcuts import render,redirect
from .forms import *
# Create your views here.

def index(request):
    form = DataForm()
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('prediction')
        
    context = {'form':form}
    return render(request,'dasboard/index.html',context)


def prediction(request):
    return render(request,'dasboard/prediction.html')