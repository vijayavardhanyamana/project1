"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views
from project import viewspatient

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('_signinn/',views.signinn,name='signinn'),
    path('signup/',views.signup,name='signup'),
    path('saveform1/',views.login,name='login'),
    path('otp/',views.otpsignp,name='otp'),
    path('query/',views.query,name='query'),
    path('forget/',views.forget,name='forget'),
    path('forget_password/',views.forget_email_otp,name='for_pas'),
    path('@otp/',views.forget_p_otp,name='for_otp'),
    
    path('patient/',viewspatient.indexpatient,name='indexpatient'),
    path('patientabout/',viewspatient.about,name='pabout'),
    path('patientservice/',viewspatient.service,name='pservice'),
    path('patientdoctors/',viewspatient.doctors,name='pdoctors'),
    path('patientappoinment/',viewspatient.appointment,name='pappointment'),
    path('patientsearch/',viewspatient.search,name='psearch'),
    path('patientcontact/',viewspatient.contact,name='pcontact'),
    path('patienteditprofile/',viewspatient.editprofile,name='peditprofile'),
    path('patienthempandsupport/',viewspatient.helpandsupport,name='phelpandsupport'),
    path('patientlogout/',viewspatient.logout,name='plogout'),
    path('patientemergencycare/',viewspatient.emergencycare,name='pemergencycare'),
    path('patientoperationandsurgery/',viewspatient.operationandsurgery,name='poperationandsurgery'),
    path('patientctscan/',viewspatient.ctscan,name='pctscan'),
    path('patientothertest/',viewspatient.othertest,name='othertest'),
    path('patientmedicineandpharmacy/',viewspatient.medicineandpharmacy,name='medicineandpharmacy'),
    #path('patientbloodtest/',viewspatient.bloodtest,name='bloodtest'),
    path('patientedit/',viewspatient.pedit,name='pedit'),

    
]
