from django.urls import path
from . import views

urlpatterns = [
    path('list_faculty/', views.list_faculty,  name='api-list_faculty'),
    path('list_school/', views.list_school,  name='api-list_school'),
    path('list_section/', views.list_section,  name='api-list_section'),
    path('list_person/', views.list_person,  name='api-list_person'),
]

