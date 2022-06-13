from django.shortcuts import render

from app.models import Activities, About, Contact, Sliders

# Create your views here.

def home(request):
   
    return render(request, 'school/home.html')


def read(request):
    return render(request, 'school/read.html')

def math(request):
    return render(request, 'school/math.html')


def color(request):
    return render(request, 'school/color.html')


def environment(request):
    return render(request, 'school/environment.html')

def comp(request):
    return render(request, 'school/computer.html')

def religion(request):
    return render(request, 'school/religion.html')
# def activities(request):
#     activities=Activities.objects.all
#     context={'activities':activities}
#     return render(request, 'school/activities.html', context)

# def activity(request,pk):
#     activityObj=Activities.objects.get(id=pk)
#     context={'activity':activityObj}
#     return render(request, 'school/detail-activity.html', context)
