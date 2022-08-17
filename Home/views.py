from django.shortcuts import render

# Create your views here.


def Home(request):
    context = {} #HomePage/footer
    return render(request, "announcement/Announcements.html", context)
    # return render(request, "HomePage/footer.html", context)

def mission(request):
    context = {}
    return render(request, "HomePage/Mission.html", context)

def vision(request):
    context = {}
    return render(request, "HomePage/Vision.html", context)
def contactUs(request):
    context = {}
    return render(request, "HomePage/ContactUs.html", context)