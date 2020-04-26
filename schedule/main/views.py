from django.shortcuts import render, redirect
import datetime

from .forms import ScheduleForm
from .models import Schedule

# Create your views here.

def schedule(request):
    data = Schedule.objects.order_by('year','month','day')
    
    params = {
        "data" : data,
    }
    
    return render(request, 'main/schedule.html', params)


def new(request):
    today = datetime.datetime.now()
    form = ScheduleForm(request.POST or None, initial={'year':today.year, 'month':today.month, 'day':today.day})

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('../')
        
    params = {
        "form" : form,
    }
    
    return render(request, 'main/new.html', params)

def edit(request):
    print(request.GET)

    for k in request.GET.keys():
        if k.isdecimal():
            ID = k
            
    data = Schedule.objects.filter(S_id = ID)
    data = data[0]

    form = ScheduleForm(request.POST or None, instance = data)
    
    if request.method == 'POST' and form.is_valid() and "change" in request.POST:
        form.save()
        return redirect('../')
    if request.method == 'POST' and "remove" in request.POST:
        Schedule.objects.filter(S_id = ID).delete()
        print(111)
        return redirect('../')
        
    params = {
        "form":form,
    }
    return render(request, 'main/edit.html', params)
