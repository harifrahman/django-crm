from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

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

# using LeadModelForm
def leadCreate(request):
    # print(request.POST)
    form = LeadModelForm()
    if request.method == 'POST':
        # print('Receiving a post from leads..')
        form = LeadModelForm(request.POST)
        if form.is_valid():                 #cleaned_data is only can access after form.is_valid()
            # print(form.cleaned_data)
            # inside we declare & do mapping manually. like below
            '''firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']

            result = Lead.objects.create(
                first_name = firstName,
                last_name = lastName,
                age = age,
                agent = agent
            )'''
            # we can simply call save, inside is_valid()
            result = form.save()

            print("Lead has been created:", result, 'id:', result.pk)
            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

def leadUpdate(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            result = form.save()
            print("Lead has been updated", result)
            return redirect("/leads/"+str(lead.pk))

    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)

# using LeadFrom
# def leadCreate(request):
#     # print(request.POST)
#     form = LeadForm()
#     if request.method == 'POST':
#         # print('Receiving a post from leads..')
#         form = LeadForm(request.POST)
#         if form.is_valid():                 #cleaned_data is only can access after form.is_valid()
#             # print('form is valid')
#             # print(form.cleaned_data)
#             firstName = form.cleaned_data['first_name']
#             lastName = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()

#             result = Lead.objects.create(
#                 first_name = firstName,
#                 last_name = lastName,
#                 age = age,
#                 agent = agent
#             )

#             print("Lead has been created", result)
#             return redirect("/leads")

#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)


# def leadUpdate(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             firstName = form.cleaned_data['first_name']
#             lastName = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']

#             lead.first_name = firstName
#             lead.last_name = lastName
#             lead.age = age
#             result = lead.save()
#             print("Lead has been updated", result)
#             return redirect("/leads")

#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)