from django.urls import path
from crm import views
urlpatterns=[
    path("api/dashboard/",views.UTILS.index),
    
]