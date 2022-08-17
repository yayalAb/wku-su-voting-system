from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ComplainForms,ResponseForms
from .models import ComplainModel,Responsemodel
from .decorators import unauthenticated_user,allowed_users
from django.db.models import Q

# Create your views here.
def complains(request):
    showall = ComplainModel.objects.all ();
    if request.user.groups.all ()[0].name == "Admin":
        showall = ComplainModel.objects.filter (comp_to="Admin")
    if request.user.groups.all ()[0].name == "Committee":
        showall = ComplainModel.objects.filter (comp_to="Committee")
    return render (request, 'complain/complains.html', {"data": showall})

@allowed_users(allowed_roles=['Voter', 'Candidate'])
def complain(request):
    form=ComplainForms()
    if request.method=="POST":
        form = ComplainModel()
        form.comp_by=request.user
        form.comp_dis=request.POST.get('comp_dis')
        form.comp_to=request.POST.get('comp_to')
        print(form.comp_by,form.comp_dis,form.comp_to)
        if ((form.comp_by is not None) and(form.comp_dis is not None) and (form.comp_to is not None)):
            form.save()
            return redirect ("complain")
    context = {'form':form}
    return render(request, "complain/ComplainForm.html", context)

def UpdateComplain(request,pk):
    complain=ComplainModel.objects.get(pk=pk)
    form = ComplainForms (instance=complain)
    if request.method=="POST":
        form = ComplainForms(request.POST,instance=complain)
        if form.is_valid():
            form.save()
            return redirect ("complain")
    context = {'form': form}

    return render (request, "complain/ComplainForm.html", context)
def DeleteComplain(request,pk):
        complain=ComplainModel.objects.get(pk=pk)
        complain.delete ()
        showall = ComplainModel.objects.all ();
        return render (request, 'complain/complains.html', {"data": showall})


@allowed_users(allowed_roles=['Admin', 'Committee'])
def Respose(request, pk):
    form=ResponseForms()
    if request.method=="POST":
        form=Responsemodel()
        form.com_id = ComplainModel.objects.get(pk=pk)
        form.comp_response = request.POST.get ('comp_response')
        form.response_by= request.user
        form.response_group= request.user.groups.all ()[0].name
        if form.comp_response is not None:
            form.save()
            return redirect ("Home")
    context = {'form': form}
    return render (request, "complain/ResponsForm.html", context)

@allowed_users(allowed_roles=['Admin', 'Committee'])
def Responses(request):
    showall = Responsemodel.objects.filter(com_id__comp_by=request.user)
    #print(showall[0].com_id.comp_by)
    #print(showall)
    #return render (request, 'complain/complains.html', {"data": showall})ComplainResponse.html
    #return HttpResponse ('You are not authorized to view this page')
    return render (request, 'complain/ComplainResponse.html', {"data": showall})
