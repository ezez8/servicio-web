from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('list_faculty/', views.FacultyList.as_view()),
    path('post_faculty/<int:pk>/', views.FacultyDetail.as_view()),

    path('list_school/', views.SchoolList.as_view()),
    path('post_school/<int:pk>/', views.SchoolDetail.as_view()),

    path('list_section/', views.list_section,  name='api-list_section'),
    path('list_person/', views.list_person,  name='api-list_person'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
