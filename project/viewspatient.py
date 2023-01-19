from django.http import HttpResponse
from django.shortcuts import render
from service.models import login1
from django.core.mail import send_mail
from django.db import connection
from service.models import profilepatient

emailid=""
fname=""
lname=""
bloodgroup=""
gender=""
phone=""
dateofbirth=""
address=""

def gain(emil,fn,ln,g):
    global emailid
    emailid=emil
    global fname
    fname=fn
    global lname
    lname=ln
    global gender
    gender=g
    
def pedit(request):
    m=""
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        bloodgroup=request.POST.get('bloodgroup')
        email=request.POST.get('email')
        gender=request.POST.get('Gender')
        phone=request.POST.get('phone')
        dateofbirth=request.POST.get('dateofbirth')
        address=request.POST.get('address')
        print(gender)
        
        a=profilepatient.objects.raw("update service_profilepatient set fname=fname,lname=lname,bloodgroup=bloodgroup,email=email,gender=gender,phone=phone,dateofbirth=dateofbirth,address=address")
        pro=profilepatient(fname=fname,lname=lname,bloodgroup=bloodgroup,email=email,gender=gender,phone=phone,dateofbirth=dateofbirth,address=address)
        pro.update()
        m="edit is success"
        
    return render(request,"indexpatient.html",{'m':m})
        
        
     
def indexpatient(request):
    n=""
    return render(request,"indexpatient.html")

def about(request):
    return render(request,"pabout.html")

def service(request):
    return render(request,"pservice.html")

def doctors(request):
    return render(request,"pteam.html")

def appointment(request):
    return render(request,"pappointment.html")

def search(request):
    return render(request,"psearch.html")

def contact(request):
    return render(request,"pcontact.html")

def editprofile(request):
    a=profilepatient.objects.raw("select * from service_profilepatient")
    
    print(a[0])
    print(a[0].fname)
    print(a[0].bloodgroup)
    return render(request,"pedit.html",{'a':a[0]})

def logout(request):
    return render(request,"home.html")



def emergencycare(request):
     return render(request,"indexpatient.html")
 
def operationandsurgery(request):
     return render(request,"indexpatient.html")
 
def ctscan(request):
     return render(request,"indexpatient.html")
 
def othertest(request):
     return render(request,"indexpatient.html")

def medicineandpharmacy(request):
     return render(request,"indexpatient.html")

def bloodtest(request):
     return render(request,"indexpatient.html")
 
def helpandsupport(request):
    return render(request,"indexpatient.html")






