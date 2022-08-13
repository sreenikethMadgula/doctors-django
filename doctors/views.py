from re import search
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from .models import Doctors
from django.db.models import Q
from django.views.decorators.csrf import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    template = loader.get_template('frontpage.html')
    return HttpResponse(template.render())   

def search_doctors(request):
    return render(
        request,
        'search_doctors.html',
        {}
    )

# @csrf_protect
@csrf_exempt
def search_results(request):
    # csrfContext = RequestContext(request)
    if request.method=="POST":
        search_doctor_query = request.POST['search_doctor_query']
        doctors = Doctors.objects.filter(Q(name__icontains=search_doctor_query) | Q(specialization__icontains=search_doctor_query) | Q(hospital__icontains=search_doctor_query))
        # doctors = Doctors.objects.values()
        print(doctors)
        if doctors:
            return render(
                request,
                'search_results.html',
                # csrfContext,
                {
                    "search_doctor_query":search_doctor_query,
                    "doctors":doctors
                    # "name":"cux",
                    # "degree":"the",
                    # "specialization":"mega",
                    # "hospital":"only",
                    # "experience":"45",
                    # "awards":"99"
                }
        )
        else:
            return render(
                request,
                'no_result.html',
                {
                    "search_doctor_query":search_doctor_query,
                }
            )
    else:
        return render(
            request,
            'doctor_profile.html',
            {
                "name":"cux",
                "degree":"the",
                "specialization":"mega",
                "hospital":"only",
                "experience":"45",
                "awards":"99"
            }
    )

def doctor_profile(request,id):
    doctor = Doctors.objects.get(id=id)
    if(doctor):
        return render(
            request,
            'doctor_profile.html',
            {
                "doctor":doctor
            }
        )       
    else:
        return render(
            request,
            HttpResponse("No profile found")
        )

# @csrf_exemptx``
def category_doctors(request,category):

    # set up pagination
    doctor_list = Doctors.objects.filter(specialization__icontains=category)
    p = Paginator(doctor_list, 5)
    page = request.GET.get('page')
    doctors = p.get_page(page)
    return render(
        request,
        'category_doctors.html',
        {
            "doctors":doctors
        }
    )

