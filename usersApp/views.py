from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from usersApp.models import *
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import *
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import json
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
from reportlab.pdfbase import ttfonts

def profile(request, institutionID = None):
    if institutionID == 0 or institutionID == None :
        pc = PC.objects.filter(institutes_id__isnull=True, university_id = request.user.university_id)

    elif institutionID != None :
        pc = PC.objects.filter( institutes_id = int(institutionID), university_id = request.user.university_id)
   
        
    context = {'user': request.user,
               'PC' :  pc,
               "Institutes":  Institutes.objects.filter( university_id = request.user.university_id)
    }

    return render(request, "usersApp/profile.html", context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            form.add_error(None, "Невірний логін ")
            context = {'form': form}
            return render(request, "usersApp/login.html", context)

        if user.password == password :
            auth.login(request, user)
            return HttpResponseRedirect(reverse("profile"))
        else:
            form.add_error(None, "Невірний пароль")
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, "usersApp/login.html", context)


def registrationWindow(request):
    return render(request, "usersApp/registration.html")

def reg(request):
    form_values = {
        'university': request.POST.get('university'),
        'email': request.POST.get('email'),
        'login': request.POST.get('login'),
        'password1': request.POST.get('password1'),
        'password2': request.POST.get('password2'),
        "status": request.POST.get("status")
    }
    
    if request.method == 'POST':
        new_University = University()
        new_University.name = form_values["university"]
        new_University.save()

        new_User = User()
        new_User.username =  form_values["login"]
        new_User.email = form_values["email"]
        new_User.university_id = new_University
        if form_values["password1"] == form_values["password2"]:
            new_User.password = form_values["password1"]
        new_User.status = form_values["status"]
        new_User.save()
        response_data = {
            'success': True,
            'message': 'User added successfully.'
        }
        return JsonResponse(response_data)
       
@login_required
def add_pc(request):
    form_values = {
        'Inventory_number': request.POST.get('Inventory_number'),
        'Model': request.POST.get('Model'),
        'Purchase_data': request.POST.get('Purchase_data'),
        'status': request.POST.get('status'),
        'Operating_System': request.POST.get('Operating_System'),
        'Processor': request.POST.get('Processor'),
        'RAM': request.POST.get('RAM'),
        'Video_cade': request.POST.get('Video_cade'),
        'Memory': request.POST.get('Memory'),
        'Office': request.POST.get('Office'),
        'Corps': request.POST.get('Corps'),
        'institution': request.POST.get('institution'),
        'image': request.FILES.get("image"),
        'oc': request.POST.get("os"),
        "description": request.POST.get("description"),
        "status": request.POST.get("status"),
    }

    if request.method == 'POST':
        new_pc = PC()
        # Встановлення значень полів
        univeID = ''.join(filter(str.isdigit, str(request.user.university_id)))
        unive = University.objects.get(id=univeID)
        new_pc.university_id = unive
        if form_values['institution'] == "null":
            new_pc.institutes_id = None
        else:
            institute_ = Institutes.objects.get(id =(form_values['institution']))
            new_pc.institutes_id = institute_

        if form_values["description"] =="":

            new_pc.description = "Опису немає"
        else:
      
             new_pc.description = form_values['description']

        if form_values['image'] != None:
            new_pc.image = form_values['image']

        new_pc.model = form_values['Model']
        new_pc.inventory_number = form_values['Inventory_number']
        new_pc.dateOfPurchase = form_values['Purchase_data']
        new_pc.processor = form_values['Processor']
        new_pc.RAM = form_values['RAM']
        new_pc.video_core = form_values['Video_cade']
        new_pc.office = form_values['Office']
        new_pc.corps = form_values['Corps']
        new_pc.status = form_values['status']
        new_pc.os = form_values['oc']
        new_pc.save()

        response_data = {
            'success': True,
            'message': 'PC added successfully.'
        }
        return JsonResponse(response_data)
    return render(request, 'usersApp/profile.html')


@login_required
def add_institution(request):
    if request.method == 'POST':
        univeID = ''.join(filter(str.isdigit, str(request.user.university_id)))
        unive = University.objects.get(id=univeID)
        name = request.POST.get("institution-name")
        new_inst = Institutes()
        new_inst.university_id = unive
        new_inst.institutes_name = name
        new_inst.save()
        response_data = {
                'success': True,
                'message': 'PC added successfully.'
            }
        return JsonResponse(response_data)
    
@login_required
def edit_pc(request):
    form_values = {
        'Inventory_number': request.POST.get('Inventory_number'),
        'Model': request.POST.get('Model'),
        'Purchase_data': request.POST.get('Purchase_data'),
        'status': request.POST.get('status'),
        'Operating_System': request.POST.get('Operating_System'),
        'Processor': request.POST.get('Processor'),
        'RAM': request.POST.get('RAM'),
        'Video_cade': request.POST.get('Video_cade'),
        'Memory': request.POST.get('Memory'),
        'Office': request.POST.get('Office'),
        'Corps': request.POST.get('Corps'),
        'institution': request.POST.get('institution'),
        'image': request.FILES.get("image"),
        'oc': request.POST.get("os"),
        "description": request.POST.get("description"),
        "status": request.POST.get("status")
    }
 
    if request.method == 'POST':
        pc = PC.objects.get(id = request.POST.get('id'))
        # Встановлення значень полів
        univeID = ''.join(filter(str.isdigit, str(request.user.university_id)))
        unive = University.objects.get(id=univeID)
       
        pc.university_id = unive
        if form_values['institution'] == "null":
            pc.institutes_id = None
        else:
            institute_ = Institutes.objects.get(id =(form_values['institution']))
            pc.institutes_id = institute_

        if form_values["description"] =="":

            pc.description = "Опису немає"
        else:
      
             pc.description = form_values['description']

        if form_values['image'] != None:
            pc.image = form_values['image']
        pc.model = form_values['Model']
        pc.inventory_number = form_values['Inventory_number']
        pc.dateOfPurchase = form_values['Purchase_data']
        pc.processor = form_values['Processor']
        pc.RAM = form_values['RAM']
        pc.video_core = form_values['Video_cade']
        pc.office = form_values['Office']
        pc.corps = form_values['Corps']
        pc.status = form_values['status']
        pc.os = form_values['oc']
        pc.save()

        response_data = {
            'success': True,
            'message': 'PC edit successfully.'
        }
        return JsonResponse(response_data)
    else:
        form = PCFormAdd()
    return render(request, 'usersApp/profile.html')

@login_required
def delete_pc(request):
    
    if request.method == 'POST':
        pc = PC.objects.get(id = request.POST.get('id'))
        pc.delete()
        response_data = {
                'success': True,
                'message': 'PC added successfully.'
            }
        return JsonResponse(response_data)
    
@login_required
def delete_institution(request):
    if request.method == 'POST':
        inst = Institutes.objects.get(id = request.POST.get('id'))
        inst.delete()
        response_data = {
                'success': True,
                'message': 'PC added successfully.'
            }
        return JsonResponse(response_data)
    

@login_required
def edit_institution(request):
    if request.method == 'POST':
        inst = Institutes.objects.get(id = request.POST.get("id"))
        name = request.POST.get("name")
        inst.institutes_name = name
        inst.save()
        response_data = {
                'success': True,
                'message': 'PC added successfully.'
            }
        return JsonResponse(response_data)
    


@login_required
def add_user(request):
    form_values = {
        'university_id': request.POST.get('university_id'),
        'login': request.POST.get('login'),
        'email': request.POST.get('email'),
        'password': request.POST.get('password'),
        'status': request.POST.get('status'),
    }
 
    if request.method == 'POST':
        university = University.objects.get(id = ''.join(filter(str.isdigit, form_values['university_id'])))
        user = User()
        user.password = form_values['password']
        user.username = form_values['login']
        user.status = form_values['status']
        user.university_id = university
        user.email = form_values['email']
        user.save()
        response_data = {
            'success': True,
            'message': 'User add successfully.'
        }
        return JsonResponse(response_data)
    else:
        form = PCFormAdd()
    return render(request, 'usersApp/profile.html')