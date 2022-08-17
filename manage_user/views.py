from random import random

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from .forms import Userforms,Key_forms
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.db.models import Q
from zk import ZK, const
import time

conn = None
zk = ZK ('192.168.1.201', port=4370, timeout=5)

@login_required (login_url='Loginpage')
@allowed_users (allowed_roles=['Admin', 'Committee'])
def showUser(request):
    if request.user.groups.all ()[0].name == "Admin":
        showall = User.objects.filter (Q (registered=True) & (Q (user_role="Committee") | Q (user_role="Admin")))
    if request.user.groups.all ()[0].name == "Committee":
        showall = User.objects.filter (Q (registered=True) & (Q (user_role="Candidate") | Q (user_role="Voter")))
    return render (request, 'user/index.html', {"data": showall})

def insertUser(request):
    if request.method == "POST":
        form = Userforms (request.POST)
        Role = request.POST.get ('user_role')
        try:
            if form.is_valid ():
                form.save ()
                messages.success (request, 'saved successfully')
                try:
                    LogRole = User.objects.get (username=request.user)
                    username = request.POST.get ('username')
                    if (LogRole.user_role == "Admin") and ((Role == "Committee") or (Role == "Admin")):
                        if (Role == "Committee"):
                            us = User.objects.filter (username=username)
                            if (fingerRigster (us.id)):
                                User.objects.filter (username=username).update (registered=True)
                        else:
                            User.objects.filter (username=username).update (registered=True)
                    if (LogRole.user_role == "Committee") and ((Role == "Voter") or (Role == "Candidate")):
                        if (Role == "Voter"):
                            us = User.objects.filter (username=username)
                            if (fingerRigster (us.id)):
                                User.objects.filter (username=username).update (registered=True)
                        else:
                            User.objects.filter (username=username).update (registered=True)
                except:
                    pass
                return render (request, 'user/insert.html')
            else:
                messages.success (request, 'error on data')
                return render (request, 'user/insert.html')
        except:
            pass
    else:
        return render (request, 'user/insert.html')
    return render (request, 'user/insert.html')


@allowed_users (allowed_roles=['Admin', 'Committee'])#Candidate
def editUser(request, id):
    editUserr = User.objects.get (id=id)
    return render (request, 'user/edit.html', {"User": editUserr})


@allowed_users (allowed_roles=['Admin', 'Committee'])
def updateUser(request, id):
    UpdateUser = User.objects.get (id=id)
    form = Userforms (request.POST, instance=UpdateUser)
    if form.is_valid ():
        form.save ()
        # if(reg==True):
        # UpdateUser.objects.filter (id=id).update (registered=True)
        messages.success (request, "successfully updated")
        showall = User.objects.filter (registered=True);
        return render (request, 'user/index.html', {"data": showall})
    else:
        messages.success (request, "Error updating")
        return render (request, 'user/edit.html', {"User": UpdateUser})


@login_required (login_url='Loginpage')
def deletUser(request, id):
    deluser = User.objects.get (id=id)
    deluser.delete ()
    showdata = User.objects.filter (registered=True);
    return render (request, 'user/index.html', {"data": showdata})


@login_required (login_url='Loginpage')
def ShowUnaprovedUser(request):
    if request.user.groups.all ()[0].name == "Admin":
        showall = User.objects.filter (Q (registered=False) & (Q (user_role="Committee") | Q (user_role="Admin")))
    if request.user.groups.all ()[0].name == "Committee":
        showall = User.objects.filter (Q (registered=False) & (Q (user_role="Candidate") | Q (user_role="Voter")))
    return render (request, 'user/AproveUser.html', {"data": showall})

@allowed_users (allowed_roles=['Admin', 'Committee'])
def aprovale(request, id):
    try:
        user = User.objects.get (id=id)
        strkey = str (random ())
        User.objects.filter (id=id).update (registered=True,key=strkey)
        print('Your Registration is  Approved, You can Create account now. and Add your fingerprint using your secret key your secret key is  ' + strkey)
        #if (fingerRigster (id)):
        send_mail (
            'Wku Student Union',
            'Your Registration is  Approved, You can Create account now. and Add your fingerprint using your secret key your secret key is  ' + strkey,
            'yayalabayneh2@gmail.com',
            [user.user_email],
            fail_silently=False,
        )
    except Exception as e:
        messages.success (request, 'Error on Approval')
    if request.user.groups.all ()[0].name == "Admin":
        showall = User.objects.filter (Q (registered=False) & (Q (user_role="Committee") | Q (user_role="Admin")))
    if request.user.groups.all ()[0].name == "Committee":
        showall = User.objects.filter (Q (registered=False) & (Q (user_role="Candidate") | Q (user_role="Voter")))
    messages.success (request, 'Approved successfully')
    return render (request, 'user/AproveUser.html', {"data": showall})

@login_required (login_url='Loginpage')
@allowed_users (allowed_roles=['Admin', 'Committee'])
def RejectUser(request, id):
    user = User.objects.get (id=id)
    send_mail (
        'Wku Student Union',
        'Sorry Your Registration Is Rejected In Same Case Please Reapply or Contact Us.',
        'yayalabayneh2@gmail.com',
        [user.user_email],
        fail_silently=False,
    )
    deluser = User.objects.get (id=id)
    deluser.delete ()
    if request.user.groups.all ()[0].name == "Admin":
        showall = User.objects.filter (Q (registered=False) & (Q (user_role="Committee") | Q (user_role="Admin")))
    if request.user.groups.all ()[0].name == "Committee":
        showall = User.objects.filter (Q (registered=False) & (Q (user_role="Candidate") | Q (user_role="Voter")))
    return render (request, 'user/AproveUser.html', {"data": showall})

def Candidates(request):
    candidates = User.objects.filter (user_role='Candidate', registered=True)
    context = {
        "candidates": candidates,
        "Title": "Candidates"
    }
    return render (request, 'user/candidates.html', context)

def Voters(request):
    candidates = User.objects.filter (user_role='Voter', registered=True)
    context = {
        "candidates": candidates,
        "Title": "Voters"
    }
    return render (request, 'user/candidates.html', context)

def Committees(request):
    Committees = User.objects.filter (user_role='Committee', registered=True)
    context = {
        "candidates": Committees,
        "Title": "Election Committees"
    }
    return render (request, 'user/candidates.html', context)

def CandidatesForVote(request):
    candidates = User.objects.filter (user_role='Candidate', registered=True)
    list = []
    for can in candidates:
        list.append (can)
    return render (request, 'user/CandidatesForVote.html', {"candidates": list})

def CandidatesForEvaluation(request):
    candidates = User.objects.filter (user_role='Candidate', registered=True)
    list = []
    for can in candidates:
        list.append (can)
    return render (request, 'user/CandidatesForEvaluation.html', {"candidates": list})

def profile(request):
    user = User.objects.get (username=request.user)
    form = Userforms (instance=user)
    if request.method == 'POST':
        form = Userforms (request.POST, request.FILES, instance=user)
        if form.is_valid ():
            form.save ()
    context = {'form': form}
    return render (request, 'user/profile.html', context)

def fingerRigster(id):
    user = User.objects.get (id=id)
    if ((user.user_role == "Voter") or (user.user_role == "Committee")):
        if (zk.connect ()):
            users1 = zk.get_users ()
            idd = (users1[len (users1) - 1].uid) + 1
            try:
                zk.verify_user (zk.enroll_user (uid=idd, temp_id=1, user_id=id))
            except:
                pass
            fp = zk.get_user_template (uid=idd, temp_id=1, user_id=id)
            print (fp.mark)
            User.objects.filter (id=id).update (user_fp=fp.mark)
            return True
    return False

@allowed_users (allowed_roles=['Voter'])
def key_check(request):
    form=Key_forms()
    context = {'form': form}
    if request.method == "POST":
        user = User.objects.get (username=request.user)
        if(request.POST.get ('key')==user.key):
            messages.success (request, 'Please put you finger in finger print Scanner')
        else:
            messages.success (request, 'invalid Key')
    return render (request, 'user/key.html', context)






