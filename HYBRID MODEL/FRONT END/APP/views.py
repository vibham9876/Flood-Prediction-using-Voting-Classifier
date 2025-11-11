from django.shortcuts import render, redirect
from . models import UserPredictModel
from . forms import UserPredictForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import pandas as pd
from django.http import HttpResponse

#from tensorflow import keras
from PIL import Image, ImageOps
from . import forms
from .models import predict
import pickle

def Landing_0(request):
    return render(request, 'welcome.html')
def aLanding(request):
    return render(request, 'welcome.html')


def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('input1')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)


def input1(request):
    return render(request,'input.html')

class_names = ['Flood',"Not Flood"]


def output(request):
    if request.method == 'POST':
        values_list = []

        values_list.append(float(request.POST.get('MonsoonIntensity')))
        values_list.append(float(request.POST.get('TopographyDrainage')))
        values_list.append(float(request.POST.get('RiverManagement')))
        values_list.append(float(request.POST.get('Deforestation')))
        values_list.append(float(request.POST.get('Urbanization')))
        values_list.append(float(request.POST.get('ClimateChange')))
        values_list.append(float(request.POST.get('DamsQuality')))
        values_list.append(float(request.POST.get('Siltation')))
        values_list.append(float(request.POST.get('AgriculturalPractices')))
        values_list.append(float(request.POST.get('Encroachments')))
        values_list.append(float(request.POST.get('IneffectiveDisasterPreparedness')))
        values_list.append(float(request.POST.get('DrainageSystems')))
        values_list.append(float(request.POST.get('CoastalVulnerability')))
        values_list.append(float(request.POST.get('Landslides')))
        values_list.append(float(request.POST.get('Watersheds')))
        values_list.append(float(request.POST.get('DeterioratingInfrastructure')))
        values_list.append(float(request.POST.get('PopulationScore')))
        values_list.append(float(request.POST.get('WetlandLoss')))
        values_list.append(float(request.POST.get('InadequatePlanning')))
        values_list.append(float(request.POST.get('PoliticalFactors')))
        algo=(request.POST.get('algo'))
        print(values_list)

        print(len(values_list))
        
        out=predict(algo,values_list)
        print(out)
        classes = class_names[int(out)]

        print(classes)

        # Now you have all the values stored in the list 'values_list'
        # You can perform your prediction logic using this list
        
        # Once you have the prediction result, you can render a response
        return render(request,'output.html',{'out':classes})  # Replace "..." with your actual prediction result
        
    else:
        # Handle GET request or other methods
        return HttpResponse("Only POST requests are allowed for this endpoint.")
def Logout(request):
    logout(request)
    return redirect('Login_3')

