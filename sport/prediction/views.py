from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('prediction')
    else:
        form = DataForm()  
    context = {
        'form':form
    }
    return render(request,'dasboard/index.html',context)


def prediction(request):
    predicted_sports = Data.objects.all()
    context = {
        'predicted_sports':predicted_sports
    }
    return render(request,'dasboard/prediction.html',context)