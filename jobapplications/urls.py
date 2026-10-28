from django.urls import path
from . import views

urlpatterns = [
    path('', views.applications_list, name='applications_list'),
    path('add/',views.add_application, name='add_application'),
    path('<int:application_id>/update/',views.update_status, name="update_status")
]
