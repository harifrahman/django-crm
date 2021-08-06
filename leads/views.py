from django.http import HttpResponse
from django.shortcuts import render
from .models import Lead

# Create your views here.

def leadList(request):
    # return HttpResponse("Hello there ~")
    # using manual template, set folder templates/leads
    # return render(request, "leads/home_page.html") 
    # but we can set views template too at setting , find DIR, and set the base dir of templates folder (views folder)
    leads = Lead.objects.all() 
    context = {
        "fullname": "John Doe",
        "type": "internship",
        "leads": leads
    }

    return render(request, "leads/lead_list.html", context)

def leadDetail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }

    # print(pk)
    # msg = "this is the detail, pk = ", pk
    # return HttpResponse(lead)
    return render(request, "leads/lead_detail.html", context)