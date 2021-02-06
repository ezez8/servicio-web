from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Faculty, School, Section, Person, Enrollment
from .serializers import FacultySerializer, SchoolSerializer, SectionSerializer, PersonSerializer

# Create your views here.

# --------------------------urls de facultad-------------------------------
@api_view(['GET'])
def list_faculty(request):
    faculty_list = Faculty.objects.all()
    serializer = FacultySerializer(faculty_list, many = True)
    return Response(serializer.data)
# --------------------------fin urls de facultad----------------------------
# --------------------------urls de escuela-------------------------------
@api_view(['GET'])
def list_school(request):
    school_list = School.objects.all()
    serializer = SchoolSerializer(school_list, many = True)
    return Response(serializer.data)
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


