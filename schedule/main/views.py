from django.shortcuts import render, redirect
from django.db.models import Q
import datetime

from .forms import ScheduleForm
from .models import Schedule

# Create your views here.

def schedule(request):
    w_list = ['月', '火', '水', '木', '金', '土', '日']
    today0 = datetime.datetime.now()
    today = "今日 : " + str(today0.month) +'/'+ str(today0.day) +'('+ w_list[today0.weekday()] + ')'
    data = Schedule.objects.order_by('year','month','day').filter(user_id=request.user.id).filter(
            Q(year__gt=today0.year)|
            Q(year=today0.year,month__gt=today0.month)|
            Q(year=today0.year,month__gte=today0.month,day__gte=today0.day)
        ).distinct()
    
    params = {
        "today": today,
        "data" : data,
    }
    
    return render(request, 'main/schedule.html', params)


def new(request):
    today = datetime.datetime.now()
    form = ScheduleForm(request.POST or None, initial={'year':today.year, 'month':today.month, 'day':today.day, 'user_id': request.user.id})

    if request.method == 'POST' and form.is_valid():
        form.save()
            
        return redirect('/schedule')
        
    params = {
        "form" : form,
    }
    
    return render(request, 'main/new.html', params)


def edit(request):
    for k in request.GET.keys():
        if k.isdecimal():
            ID = k
            
    data = Schedule.objects.filter(S_id = ID)
    data = data[0]

    form = ScheduleForm(request.POST or None, instance = data)
    
    if request.method == 'POST' and form.is_valid() and "change" in request.POST:
        form.save()
        return redirect('/schedule')
    if request.method == 'POST' and "remove" in request.POST:
        Schedule.objects.filter(S_id = ID).delete()

        return redirect('/schedule')
        
    params = {
        "form":form,
    }
    return render(request, 'main/edit.html', params)

def past(request):
    today = datetime.datetime.now()

    data = Schedule.objects.order_by('year','month','day').filter(
            Q(year__lt=today.year)|
            Q(year=today.year,month__lt=today.month) |
            Q(year=today.year,month__lt=today.month,day__lt=today.day)
        ).distinct()

    params = {
        "data" : data,
    }

    return render(request, 'main/past.html', params)

