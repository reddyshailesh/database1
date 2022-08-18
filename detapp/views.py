import imp
import re
from django.shortcuts import render
from .models import details
from django.http import JsonResponse
import json

# Create your views here.

def indexpage(req):
    return render(req,'index.html')

def newpage(request):
    na=request.POST.get("Names")
    ag=request.POST.get("ages")
    jo=request.POST.get("jobs")
    add=request.POST.get("add")

    o_ref=details(name=na, age=ag, job=jo, address=add)
    o_ref.save()
    return render(request, 'index.html',{"message":"next"})

def json(request):
    data = list(details.objects.values())
    return JsonResponse(data, safe=False)