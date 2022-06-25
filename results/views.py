from django.shortcuts import render
from .models import Result
from django.views.generic import ListView
# from django.http import JsonResponse
# from django.shortcuts import HttpResponse
# from results.models import Results



def Results(request):
    results=Result.objects.all()
    context={'results':results}
    return render(request, 'quizes/results.html', context)
