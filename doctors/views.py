from pydoc import doc
from re import search
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader,RequestContext
from django.db.models import Q
from django.views.decorators.csrf import *
from django.core.paginator import Paginator

# from doctors import serializers
from .serializers import DoctorSerializer

from .models import Doctors
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



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


# @api_view(['GET'])
# def doctor_list(request):
    # doctor_list = Doctors.objects.all()
    # serializer = DoctorSerializer(doctor_list,many=True)
    # return Response(serializer.data)

# @api_view(['POST'])
# def add_doctor(request):
    # serializer = DoctorSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data,status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT','DELETE'])
# def doctor_profile(request,id):
    # try:
    #     doctor = Doctors.objects.get(pk=id)
    # except Doctors.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

#     if(request.method=='GET'):
        # serializer = DoctorSerializer(doctor)
        # return Response(serializer.data)
    
#     elif(request.method=='PUT'):
        # serializer = DoctorSerializer(doctor, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     elif(request.method=='DELETE'):
        # doctor.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorList(APIView):
    def get(self,requst):
        doctor_list = Doctors.objects.all()
        serializer = DoctorSerializer(doctor_list,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class DoctorProfile(APIView):
    def get_doctor_by_id(self,id):
        try:
            return Doctors.objects.get(pk=id)
        except Doctors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        doctor = self.get_doctor_by_id(id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    
    def put(self,request,id):
        doctor = self.get_doctor_by_id(id)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        doctor = self.get_doctor_by_id(id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)