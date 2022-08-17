from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ExamForms,AnsForms
from .models import exam_model,ExamresultModel
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
@allowed_users (allowed_roles=['Committee'])#Candidate
def AddExamQst(request):
    form=ExamForms()
    if request.method=="POST":
        form = ExamForms (request.POST)
        if form.is_valid():
            form.save()
            return redirect ("AddExamQst")
    context = {'form':form}
    return render(request, "Exam/add_exam_qst.html", context)

@allowed_users (allowed_roles=['Committee'])#Candidate
def Questions(request):
    exams = exam_model.objects.all ()
    return render (request, 'Exam/Questions.html',{"data":exams})

@allowed_users (allowed_roles=['Candidate'])#Candidate
def Exams(request,num,res):
    exams = exam_model.objects.all ()
    ii=1;
    for i in exams:
        if(ii==len(exams)):
            if (i.answer == request.POST.get ('cho')):
                res = res + 1
            result=((res*10)/len(exams))
            candi=ExamresultModel.objects.get (username=request.user)
            t40=candi.Total_40+result
            t100=candi.Total_100+result
            ExamresultModel.objects.filter (username=request.user).update (written_exam=result, Total_40=t40,Total_100=t100)
            return HttpResponse ('10Q  Successfully finished, you get '+str(result)+" out of 10")
        if(ii==num-1):
            if request.method == "POST":
                print (request.POST.get ('cho'))
                if (i.answer == request.POST.get ('cho')):
                    res = res + 1
            context = {
                   "num": ii+2,
                   "num1": ii+1,
                   "res":res,
                   "data": exams[ii]}
            return render (request, 'Exam/Exams_Question.html', context)
        ii = ii + 1
    return render (request, 'Exam/Exams_Question.html')

@allowed_users (allowed_roles=['Candidate'])#Candidate
def Exams1(request):
    exams = exam_model.objects.all ()
    context = {"num": 2,
               "num1": 1,
               "res": 0,
               "data": exams[0]}
    return render (request, 'Exam/Exams_Question.html', context)

@allowed_users (allowed_roles=['Admin','Committee'])#Candidate
def DeleteExams(request):
    exams = exam_model.objects.all ()
    exams.delete()
    return render (request, 'Exam/Exams_Question.html', {"data": exams})

@allowed_users (allowed_roles=['Committee'])#Candidate
def UpdateQuestions(request,pk):
    campaign=exam_model.objects.get(id=pk)
    form = ExamForms (instance=campaign)
    if request.method=="POST":
        form = ExamForms (request.POST,instance=campaign)
        if form.is_valid():
            form.save()
            return redirect ("Questions")
    context = {'form': form}
    return render (request, "Exam/add_exam_qst.html", context)

@allowed_users (allowed_roles=['Committee'])#Candidate
def DeleteQuestion(request, pk):
    qus = exam_model.objects.get (id=pk)
    qus.delete ()
    exams = exam_model.objects.all ();
    return render (request, 'Exam/Questions.html', {"data": exams})


