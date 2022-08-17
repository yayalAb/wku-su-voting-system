from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import ScheduleForms
from .models import ScheduleModel

# Create your views here.
def Schedules(request):
    showall = ScheduleModel.objects.all ();
    return render (request, 'voting_day/Schedules.html', {"data": showall})


def Schedule(request):
    form=ScheduleForms()
    if request.method=="POST":
        form = ScheduleForms (request.POST)
        if form.is_valid():
            form.save()
            return redirect ("Schedules")

    context = {'form':form}
    return render(request, "voting_day/Schedule.html", context)

def UpdateSchedule(request,pk):
    anouncment=ScheduleModel.objects.get(id=pk)
    form = ScheduleForms (instance=anouncment)
    if request.method=="POST":
        form = ScheduleForms (request.POST,instance=anouncment)
        if form.is_valid():
            form.save()
            return redirect ("Schedules")
    context = {'form': form}
    return render (request, "voting_day/Schedule.html", context)
def DeleteSchedule(request,pk):
        anouncment=ScheduleModel.objects.get(id=pk)
        anouncment.delete ()
        showall = ScheduleModel.objects.all ();
        return render (request, 'voting_day/Schedules.html', {"data": showall})

