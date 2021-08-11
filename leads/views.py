from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail 
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm

# Create your views here.
# Classed based views sample

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    context_object_name="lead"

    def get_success_url(self):
        return reverse("login")

class LandingPageView(TemplateView):
    template_name = "landing.html"

def landingPage(request):
    return render(request, "landing.html")

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    '''
    the context by default this class assign is "object_list"
    but we can to overwrite the context name like this
    '''
    context_object_name="leads"

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

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    # no need to specify, like using get(id=pk). Auto grep by django it self ;P
    queryset = Lead.objects.all()
    context_object_name="lead"

def leadDetail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }

    # print(pk)
    # msg = "this is the detail, pk = ", pk
    # return HttpResponse(lead)
    return render(request, "leads/lead_detail.html", context)

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    # no need write with '()'. just type to specify form, cause this for create -> form_class = LeadModelForm()
    form_class = LeadModelForm
    context_object_name="lead"

    def get_success_url(self):
        # return redirect("/leads")
        # instead of returning hard code like above, we can pass using name of url. using reverse from shortcut
        return reverse("leads:lead-list")

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject="New Lead created",
            message="Visit this url for checking: ",
            from_email="test@test.com",
            recipient_list=[
                "recipent@test.com"
            ]
        )
        return super(LeadCreateView, self).form_valid(form)

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


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    # need queryset, caused we need to know which id, we wanna update
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    context_object_name="lead"

    def get_success_url(self):
        return reverse("leads:lead-list")

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


class LeadDeleteView(DeleteView):
    # need to make new template.html for deleting. like a simple confirmation for delete data
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    context_object_name="lead"

    def get_success_url(self):
        return reverse("leads:lead-list")

def leadDelete(request, pk):
    lead = Lead.objects.get(id=pk)
    id = lead.pk
    lead.delete()
    print('success deleting lead:', lead.first_name, lead.last_name, "with id:", id)
    return redirect("/leads")

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