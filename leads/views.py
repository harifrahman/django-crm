from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homePage(request):
    # return HttpResponse("Hello there ~")
    # using manual template, set folder templates/leads
    # return render(request, "leads/home_page.html") 
    # but we can set views template too at setting , find DIR, and set the base dir of templates folder (views folder)
    return render(request, "second_page.html")