from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from .models import Faculty, School, Section, Person, Enrollment
from .serializers import FacultySerializer, SchoolSerializer, SectionSerializer, PersonSerializer

# Create your views here.

# --------------------------urls de facultad-------------------------------

class FacultyList(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

# --------------------------fin urls de facultad----------------------------
# --------------------------urls de escuela-------------------------------

class SchoolList(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

# --------------------------fin urls de escuela---------------------------
# --------------------------urls de seccion-------------------------------
@api_view(['GET'])
def list_section(request):
    section_list = Section.objects.all()
    serializer = SectionSerializer(section_list, many = True)
    return Response(serializer.data)
# --------------------------fin urls de seccion---------------------------
# --------------------------urls de persona-------------------------------
@api_view(['GET'])
def list_person(request):
    person_list = Person.objects.all()
    serializer = PersonSerializer(person_list, many = True)
    return Response(serializer.data)
# --------------------------fin urls de persona---------------------------


