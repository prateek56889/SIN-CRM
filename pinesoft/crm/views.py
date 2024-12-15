from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
from .models import clients,Notification
from rest_framework.response import Response
from rest_framework.decorators import api_view
class UTILS:
    @api_view(["GET"])
    def index(request):
        query=len([i for i in clients.objects.filter(Status="query")])
        sales=len([i for i in clients.objects.filter(Status="sales")])
        closed=len([i for i in clients.objects.filter(Status="closed")])
        return Response(data={"query":query,"sales":sales,"closed":closed,"max":query+sales+closed})
        



