from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import CampaignForms,campaign_videoForm,evaluation_videoFrom
from .models import CampaignModel,campaign_video,evaluation_video,VotingModel
from .models import  fileUploading
from django.contrib import messages
from .forms import fileUploadingForms
# Create your views here.
def Campaigns(request):
    showall = CampaignModel.objects.all ();
    return render (request, 'campaign/campaigns.html', {"data": showall})

def Campaign(request):
    form=CampaignForms()
    if request.method=="POST":
        form = CampaignForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("Campaigns")
    context = {'form':form}
    return render(request, "campaign/Campaign.html", context)

def UpdateCampaign(request,pk):
    campaign=CampaignModel.objects.get(id=pk)
    form = CampaignForms (instance=campaign)
    if request.method=="POST":
        form = CampaignForms (request.POST,instance=campaign)
        if form.is_valid():
            form.save()
            return redirect ("Campaign")
    context = {'form': form}
    return render (request, "campaign/Campaign.html", context)
def DeleteCampaign(request,pk):
        campaign=CampaignModel.objects.get(id=pk)
        campaign.delete ()
        showall = CampaignModel.objects.all ();
        return render (request, 'campaign/Campaign.html', {"data": showall})

def campaignUpload(request):
    form = campaign_videoForm ()
    if request.method == "POST":
        form = campaign_videoForm (request.POST,request.FILES)
        if form.is_valid ():
            form.save ()
            return redirect ("campaignUpload")
    context = {'form': form}
    return render (request, "campaign/FileUpload.html", context)

def campaign_videos(request):
    cert = campaign_video.objects.filter(approval=True)
    return render (request, 'campaign/campaign_videos.html', {"data": cert})

def approvale_need_campaign(request):
    Videos = campaign_video.objects.filter(approval=False)
    return render (request, 'campaign/campaign_videos.html', {"data": Videos})

def approve_campaign(request, id):
    campaign_video.objects.get(id=id).update (approval=True)
    Videos = campaign_video.objects.filter(approval=False)
    return render (request, 'campaign/campaign_videos.html', {"data": Videos})

def delete_campaign(request,id):
    campaign = campaign_video.objects.get (id=id)
    campaign.delete ()
    showall = campaign_video.objects.all ();
    return render (request, 'campaign/campaign_videos.html', {"data": showall})

def EvaluationUpload(request):
    form = evaluation_videoFrom ()
    if request.method == "POST":
        form = evaluation_videoFrom (request.POST,request.FILES)
        if form.is_valid ():
            form.save ()
            return redirect ("EvaluationUpload")
    context = {'form': form}
    return render (request, "campaign/FileUpload.html", context)

def Evaluation_videos(request):
    cert = evaluation_video.objects.filter(approval=True)
    return render (request, 'campaign/Evaluation_videos.html', {"data": cert})

#@allowed_users (allowed_roles=['Admin', 'Committee'])
def approvale_need_evaluation(request):
    Videos = evaluation_video.objects.filter(approval=False)
    return render (request, 'campaign/Evaluation_videos.html', {"data": Videos})

def approve_evaluation(request, id):
    evaluation_video.objects.filter(id=id).update(approval=True)
    Videos = evaluation_video.objects.filter(approval=False)
    return render (request, 'campaign/Evaluation_videos.html', {"data": Videos})

def delete_Evaluation(request, id):
    campaign = evaluation_video.objects.get (id=id)
    campaign.delete ()
    showall = evaluation_video.objects.all ();
    return render (request, 'campaign/Evaluation_videos.html', {"data": showall})

def DocumentUpload(request):
    form = fileUploadingForms ()
    if request.method == "POST":
        form = fileUploadingForms (request.POST,request.FILES)
        if form.is_valid ():
            form.save ()
            return redirect ("DocumentUpload")
    context = {'form': form}
    return render (request, "campaign/FileUpload.html", context)

def certificates(request):
    cert = fileUploading.objects.filter(approval=True)
    return render (request, 'campaign/certificates.html', {"data": cert})

def approvale_need_certificates(request):
    certificates = fileUploading.objects.filter(approval=False)
    return render (request, 'campaign/certificates.html', {"data": certificates})

def approve_certificates(request, id):
    us=fileUploading.objects.filter(id=id).update (approval=True)
    username="yayal@cnd"#us.username
    cert=fileUploading.objects.filter(username=username,approval=True)
    if(len(cert)>=4):
        res=5
    else:
        res= (5*len(cert))/4
    print(res)
    resa=VotingModel.objects.get(username=username)
    t40=resa.Total_40 + res
    t100=resa.Total_100 + res
    VotingModel.objects.filter (username=username).update (certifcate=res,Total_40=t40,Total_100=t100)
    certificates = fileUploading.objects.filter(approval=False)
    return render (request, 'campaign/certificates.html', {"data": certificates})

def delete_certificates(request, id):
    file = fileUploading.objects.get (id=id)
    file.delete ()
    showall = fileUploading.objects.all ();
    return render (request, 'campaign/certificates.html', {"data": showall})


