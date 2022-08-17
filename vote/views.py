from django.shortcuts import render, redirect
from .forms import VotingForms, EvaluationForms
from .models import VotingModel,voter,Voters,Election_Committe,Users
from django.contrib.auth.decorators import  login_required
from django.contrib import messages
#from ..Account.decorators import allowed_users
from zk import ZK, const
import time
from .decorators import unauthenticated_user,allowed_users

conn = None
zk = ZK('192.168.1.201', port=4370, timeout=5)

def  changeStatusEc(username1,name,isVote):
    cand= VotingModel.objects.all ()
    username=username1
    votr_sta = Election_Committe.objects.get (username=username1)
    i=0
    for item in cand:
        print(username1)
        print(name)
        print(item.username)
        if item.username==name and i==0:
            print(True)
            if votr_sta.cand1 == False:
                Election_Committe.objects.filter (username=username).update (stat=True,cand1=True)
                print(True)
                isVote = True
        elif item.username == name and i == 1:
            if votr_sta.cand2 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand2=True)
                isVote = True
        elif item.username == name and i == 2:
            if votr_sta.cand3 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand3=True)
                isVote = True
        elif item.username == name and i == 3:
            if votr_sta.cand4 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand4=True)
                isVote = True
        elif item.username == name and i == 4:
            if votr_sta.cand5 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand5=True)
                isVote = True
        elif item.username == name and i == 5:
            if votr_sta.cand6 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand6=True)
                isVote = True
        elif item.username == name and i == 6:
            if votr_sta.cand7 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand7=True)
                isVote = True
        elif item.username == name and i == 7:
            if votr_sta.cand8 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand8=True)
                isVote = True
        elif item.username == name and i == 8:
            if votr_sta.cand9 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand9=True)
                isVote = True
        elif item.username == name and i == 9:
            if votr_sta.cand10 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand10=True)
                isVote = True
        elif item.username == name and i == 10:
            if votr_sta.cand11 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand11=True)
                isVote = True
        elif item.username == name and i == 11:
            if votr_sta.cand12 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand12=True)
                isVote = True
        elif item.username == name and i == 12:
            if votr_sta.cand13 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand13=True)
                isVote = True
        elif item.username == name and i == 13:
            if votr_sta.cand14 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand14=True)
                isVote = True
        elif item.username == name and i == 14:
            if votr_sta.cand15 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand15=True)
                isVote = True
        elif item.username == name and i == 15:
            if votr_sta.cand16 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand16=True)
                isVote = True
        elif item.username == name and i == 16:
            if votr_sta.cand17 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand17=True)
                isVote = True
        elif item.username == name and i == 17:
            if votr_sta.cand18 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand18=True)
                isVote = True
        elif item.username == name and i == 18:
            if votr_sta.cand19 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand19=True)
                isVote = True
        elif item.username == name and i == 19:
            if votr_sta.cand20 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand20=True)
                isVote = True
        elif item.username == name and i == 20:
            if votr_sta.cand21 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand21=True)
                isVote = True
        elif item.username == name and i == 21:
            if votr_sta.cand22 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand22=True)
                isVote = True
        elif item.username == name and i == 22:
            if votr_sta.cand23 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand23=True)
                isVote = True
        elif item.username == name and i == 23:
            if votr_sta.cand24 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand24=True)
                isVote = True
        elif item.username == name and i == 24:
            if votr_sta.cand25 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand25=True)
                isVote = True
        elif item.username == name and i == 25:
            if votr_sta.cand26 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand26=True)
                isVote = True
        elif item.username == name and i == 26:
            if votr_sta.cand27 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand27=True)
                isVote = True
        elif item.username == name and i == 27:
            if votr_sta.cand28 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand28=True)
                isVote = True
        elif item.username == name and i == 28:
            if votr_sta.cand29 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand29=True)
                isVote = True
        elif item.username == name and i == 29:
            if votr_sta.cand30 == False:
                Election_Committe.objects.filter (username=username).update (stat=True, cand30=True)
                isVote = True
        else:
            if not isVote:
                return False
        i=i+1
        if isVote:
            return True
    return False


def  changeStatus(username1,name,isVote):
    cand= VotingModel.objects.all ()
    username=username1
    votr_sta = Voters.objects.get (username=username)
    i=0
    for item in cand:
        if item.username==name and i==0:
            if votr_sta.cand1 == False:
                Voters.objects.filter (username=username).update (stat=True,cand1=True)
                isVote = True
        elif item.username == name and i == 1:
            if votr_sta.cand2 == False:
                Voters.objects.filter (username=username).update (stat=True, cand2=True)
                isVote = True
        elif item.username == name and i == 2:
            if votr_sta.cand3 == False:
                Voters.objects.filter (username=username).update (stat=True, cand3=True)
                isVote = True
        elif item.username == name and i == 3:
            if votr_sta.cand4 == False:
                Voters.objects.filter (username=username).update (stat=True, cand4=True)
                isVote = True
        elif item.username == name and i == 4:
            if votr_sta.cand5 == False:
                Voters.objects.filter (username=username).update (stat=True, cand5=True)
                isVote = True
        elif item.username == name and i == 5:
            if votr_sta.cand6 == False:
                Voters.objects.filter (username=username).update (stat=True, cand6=True)
                isVote = True
        elif item.username == name and i == 6:
            if votr_sta.cand7 == False:
                Voters.objects.filter (username=username).update (stat=True, cand7=True)
                isVote = True
        elif item.username == name and i == 7:
            if votr_sta.cand8 == False:
                Voters.objects.filter (username=username).update (stat=True, cand8=True)
                isVote = True
        elif item.username == name and i == 8:
            if votr_sta.cand9 == False:
                Voters.objects.filter (username=username).update (stat=True, cand9=True)
                isVote = True
        elif item.username == name and i == 9:
            if votr_sta.cand10 == False:
                Voters.objects.filter (username=username).update (stat=True, cand10=True)
                isVote = True
        i=i+1
        if isVote:
            return True
    return False

# Create your views here.
#@login_required(login_url='Loginpage')
@allowed_users(allowed_roles=['Voter'])
def Voting(request,username):
    form=VotingForms()
    if request.method=="POST":
        form = VotingForms(request.POST)
        candidate =username
        if candidate is not None:
            query = VotingModel.objects.get (username=candidate)
            pro = query.protocol + float(form.data.get ('protocol'))
            pre = query.presentation_skill + float(form.data.get ('presentation_skill'))
            conf = query.confidence + float(form.data.get ('confidence'))
            stra = query.strategic_plane + float(form.data.get ('strategic_plane'))
            ans = query.answering + float(form.data.get ('answering'))
            tm = query.Time_management + float(form.data.get ('Time_management'))
            total=tm+ans+stra+conf+pre+pro
            total_100=query.Total_40+total
            if changeStatus (request.user,candidate,False):
                try:
                #     conn = zk.connect ()
                #     messages.info (request, "Connecting to device...")
                # except Exception as e:
                #     messages.info (request, "Device Not Connecting please check Connection ...")
                # if (zk.connect ()):
                #     messages.info (request, "Connected Successfully")
                #     messages.info (request, "Please put your finger in fingerprint Sensor on 5 second")
                #     time.sleep (5)
                #     aten = conn.get_attendance ()
                #     fp_id=aten[len (aten)-1].user_id
                #     us=Users.objects.get (username=request.user)
                #     if(int(fp_id)==us.id):
                        messages.success (request, "voted Successfully")
                        VotingModel.objects.filter (username=candidate).update (protocol=pro, presentation_skill=pre,
                                                                                confidence=conf, strategic_plane=stra,
                                                                                answering=ans, Time_management=tm,
                                                                                Total_60=total,
                                                                                Total_100=total_100)

                        messages.success (request, "voted Successfully")
                except Exception as e:
                    messages.success (request, "error on  vote ",e)
                    #     conn.test_voice (0)
                    # else:
                    #     conn.test_voice (30)
                    #     conn.test_voice (4)
                    #     messages.success (request," your Fingerprint not mache")
            else:
               messages.error (request, "you voted before")
            #return redirect ("CandidatesForVote")
    context = {'form':form,
               'username':username}
    return render(request, "vote/votingform.html", context)

@login_required(login_url='Loginpage')
def Evaluate(request,username):
    form=EvaluationForms()
    if request.method=="POST":
        form = EvaluationForms (request.POST)
        candidate = username
        if candidate is not None:
            query = VotingModel.objects.get (username=candidate)
            cer = query.certifcate # + float (form.data.get ('certifcate'))
            wrex = query.written_exam #+ float (form.data.get ('written_exam'))
            orin = query.oral_interview + float (form.data.get ('oral_interview'))
            stra = query.Str_and_opra_plane + float (form.data.get ('Str_and_opra_plane'))
            total = cer+wrex+orin+stra
            total_100 = query.Total_60 + total
            if changeStatusEc(request.user, candidate, False):
                VotingModel.objects.filter (username=candidate).update (certifcate=cer, written_exam=wrex,
                                                                        oral_interview=orin, Str_and_opra_plane=stra,
                                                                        Total_40=total, Total_100=total_100)
                messages.success (request, "voted Successfully")
                return redirect ("CandidatesForEvaluation")
            else:
                messages.error (request, "voted before")

    context = {'form': form,
               'username':username}
    return render (request, "vote/EvaluationForm.html", context)

def fingerprint(request):
    messages.info (request, "Connecting to device...")
    try:
        conn = zk.connect ()
        if (zk.connect ()):
            messages.info (request, "Connected Successfully")
            messages.info (request, "Please put your finger in fingerprint Sensor")
            try:
                conn.enroll_user (uid=1, temp_id=1, user_id='4')
                messages.success (request, "Registered Successfully thank you")
                zk.test_voice (index=0)
            except Exception as e:
                messages.error (request, e)
    except Exception as e:
        messages.error(request, "Device not Connected Successfully",e)
    return render (request, "vote/Fingerprint.html")

def ViewResult(request):
    Results = VotingModel.objects.all ()
    count=Voters.objects.filter (stat=True)
    countEc = Election_Committe.objects.filter (stat=True)
    list=[]
    for res in Results:
        t4=res.Total_40 = (res.Total_40 / len (countEc))
        t6=res.Total_60 = (res.Total_60 / len (count))
        res.Total_100 = t4+t6
        list.append(res)
    return render (request, 'vote/Results.html', {"Results": list})

def ViewResult40(request):
    Results = VotingModel.objects.all ()
    count = Voters.objects.filter (stat=True)
    countEc = Election_Committe.objects.filter (stat=True)
    list = []
    for res in Results:
        res.oral_interview = (res.oral_interview / len (countEc))
        res.Str_and_opra_plane = (res.Str_and_opra_plane / len (countEc))
        res.Total_40 = (res.Total_40 / len (countEc))
        list.append (res)
    return render (request, 'vote/Results40.html', {"Results": list})

def ViewResult60(request):
    Results = VotingModel.objects.all ()
    count = Voters.objects.filter (stat=True)
    list = []
    for res in Results:
        res.protocol = (res.protocol / len (count))
        res.presentation_skill = (res.presentation_skill / len (count))
        res.confidence = (res.confidence / len (count))
        res.strategic_plane = (res.strategic_plane / len (count))
        res.answering = (res.answering / len (count))
        res.Time_management = (res.Time_management / len (count))
        res.Total_60 = (res.Total_60 / len (count))
        list.append (res)
    return render (request, 'vote/Results60.html', {"Results": list})

