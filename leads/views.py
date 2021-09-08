from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.
def home(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    # return HttpResponse('oyyyy')
    return render(request, "leads/home.html", context)