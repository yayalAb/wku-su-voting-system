from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import AnnounceModelForms
from .models import AnnounceModel

# Create your views here.
def Announcement(request):
    showall = AnnounceModel.objects.all ();
    return render (request, 'announcement/Announcements.html', {"data": showall})

def ManageAnnouncement(request):
    showall = AnnounceModel.objects.all ();
    return render (request, 'announcement/ManageAnnouncements.html', {"data": showall})

def Announce(request):
    form=AnnounceModelForms()
    if request.method=="POST":
        form = AnnounceModelForms (request.POST)
        if form.is_valid():
            form.save()
            return redirect ("Announcement")

    context = {'form':form}
    return render(request, "announcement/AnnouncementForm.html", context)

def UpdateAnnounce(request,pk):
    anouncment=AnnounceModel.objects.get(id=pk)
    form = AnnounceModelForms (instance=anouncment)
    if request.method=="POST":
        form = AnnounceModelForms (request.POST,instance=anouncment)
        if form.is_valid():
            form.save()
            return redirect ("Announce")
    context = {'form': form}
    return render (request, "announcement/AnnouncementForm.html", context)




def DeleteAnnounce(request,pk):
        anouncment=AnnounceModel.objects.get(id=pk)
        anouncment.delete ()
        showall = AnnounceModel.objects.all ();
        return render (request, 'announcement/Announcements.html', {"data": showall})

