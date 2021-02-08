from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('faculty_list/', views.FacultyList.as_view()),
    path('faculty_detail/<int:pk>/', views.FacultyDetail.as_view()),

    path('school_list/', views.SchoolList.as_view()),
    path('school_detail/<int:pk>/', views.SchoolDetail.as_view()),

    path('section_list/', views.SectionList.as_view()),
    path('section_detail/<int:pk>/', views.SectionDetail.as_view()),

    path('person_list/', views.PersonList.as_view()),
    path('person_detail/<int:pk>/', views.PersonDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
